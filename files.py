import os
import json
import time
from security import sanitize_filename, is_safe_path

WORKSPACE_DIR = os.path.abspath("jobs")

def create_job_workspace(job_id: str) -> str:
    job_dir = os.path.join(WORKSPACE_DIR, job_id)
    subdirs = ["input", "extracted", "generated", "logs", "responses"]
    for sd in subdirs:
        os.makedirs(os.path.join(job_dir, sd), exist_ok=True)
    return job_dir

def save_job_file(job_id: str, filename: str, content: bytes, folder="input") -> str:
    job_dir = create_job_workspace(job_id)
    clean_filename = sanitize_filename(filename)
    target_dir = os.path.join(job_dir, folder)
    target_path = os.path.join(target_dir, clean_filename)

    if not is_safe_path(target_dir, target_path):
        raise ValueError("Invalid target path detected (path traversal attempt).")

    with open(target_path, "wb") as f:
        f.write(content)

    return target_path

def save_job_response(job_id: str, round_num: int, node_id: str, data: dict):
    job_dir = create_job_workspace(job_id)
    filename = f"round_{round_num}_{node_id}.json"
    target_path = os.path.join(job_dir, "responses", filename)
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def extract_text_from_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return ""
    ext = os.path.splitext(filepath)[1].lower()
    if ext in [".txt", ".md", ".json", ".csv", ".py", ".html", ".js", ".css", ".yaml", ".yml"]:
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception:
            return ""
    return f"[Binary or non-plain-text file uploaded: {os.path.basename(filepath)}]"
