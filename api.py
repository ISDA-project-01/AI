import os
from flask import Flask, request, jsonify, send_from_directory
from main import MasterCoordinator
from auth import authenticate_user, verify_session, revoke_session
from health import update_node_heartbeat, get_cluster_health
from monitor import get_system_metrics
from files import save_job_file, extract_text_from_file
from voice import VoiceProcessor
from vision import get_vision_provider
from security import sanitize_filename

app = Flask(__name__, static_folder='.', static_url_path='')
master = MasterCoordinator()
voice_proc = VoiceProcessor()
vision_proc = get_vision_provider()

# Middleware for auth
def require_auth(roles=None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            session = verify_session(token)
            if not session:
                return jsonify({"error": "Unauthorized"}), 401
            if roles and session.get("role") not in roles:
                return jsonify({"error": "Forbidden"}), 403
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

# UI Static Routes
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/admin')
def serve_admin():
    return send_from_directory('.', 'administration.html')

@app.route('/supervisor')
def serve_supervisor():
    return send_from_directory('.', 'supervisor.html')

# API Endpoints
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    token = authenticate_user(username, password)
    if token:
        session = verify_session(token)
        return jsonify({"token": token, "role": session["role"], "username": username})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    revoke_session(token)
    return jsonify({"message": "Logged out successfully"})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json or {}
    prompt = data.get("prompt", "")
    web_search = data.get("web_search", False)
    if not prompt:
        return jsonify({"error": "Prompt required"}), 400

    job_res = master.run_job(prompt, enable_web_search=web_search)
    return jsonify(job_res)

@app.route('/api/voice', methods=['POST'])
def handle_voice():
    if 'file' not in request.files:
        return jsonify({"error": "Audio file required"}), 400
    file = request.files['file']
    filename = sanitize_filename(file.filename)
    save_path = os.path.join("jobs", "temp_voice_" + filename)
    file.save(save_path)

    transcribed = voice_proc.speech_to_text(save_path)
    job_res = master.run_job(transcribed)

    tts_path = os.path.join("jobs", "tts_output_" + job_res["job_id"] + ".wav")
    voice_proc.text_to_speech(job_res["final_synthesis"], tts_path)

    return jsonify({
        "transcription": transcribed,
        "job": job_res,
        "tts_file": tts_path
    })

@app.route('/api/files', methods=['POST'])
def handle_file():
    if 'file' not in request.files:
        return jsonify({"error": "File required"}), 400
    file = request.files['file']
    prompt = request.form.get("prompt", "Analyze the uploaded file.")

    job_id = f"JOB-FILE-{os.urandom(4).hex()}"
    saved_path = save_job_file(job_id, file.filename, file.read())
    extracted_text = extract_text_from_file(saved_path)

    full_prompt = f"{prompt}\n\nFile Content ({file.filename}):\n{extracted_text}"
    job_res = master.run_job(full_prompt)
    return jsonify(job_res)

@app.route('/api/image', methods=['POST'])
def handle_image():
    if 'file' not in request.files:
        return jsonify({"error": "Image file required"}), 400
    file = request.files['file']
    prompt = request.form.get("prompt", "Describe this image.")

    job_id = f"JOB-IMG-{os.urandom(4).hex()}"
    saved_path = save_job_file(job_id, file.filename, file.read())

    vision_analysis = vision_proc.analyze_image(saved_path, prompt)
    full_prompt = f"{prompt}\n\nVision Analysis:\n{vision_analysis}"

    job_res = master.run_job(full_prompt)
    return jsonify(job_res)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "cluster_health": get_cluster_health(),
        "system_metrics": get_system_metrics()
    })

@app.route('/api/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json or {}
    node_id = data.get("node_id")
    if node_id:
        update_node_heartbeat(node_id, data)
        return jsonify({"status": "acknowledged"})
    return jsonify({"error": "node_id required"}), 400

@app.route('/api/supervisor/command', methods=['POST'])
@require_auth(roles=["supervisor", "admin"])
def supervisor_command():
    data = request.json or {}
    command = data.get("command")
    job_id = data.get("job_id")

    if command == "CANCEL_JOB" and job_id in master.jobs:
        master.jobs[job_id]["status"] = "CANCELLED"
        return jsonify({"message": f"Job {job_id} cancelled"})

    return jsonify({"message": f"Command {command} processed successfully"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    print(f"Starting VAPIC Master Gateway API on port {port}...")
    app.run(host='0.0.0.0', port=port)
