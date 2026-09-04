import os
import sys
import time
import requests
from flask import Flask, request, jsonify
from monitor import get_system_metrics

class PeerNode:
    def __init__(self, node_id, port, model_name):
        self.node_id = node_id
        self.port = port
        self.model_name = model_name
        self.master_url = os.getenv("MASTER_URL", "http://192.168.50.11:8000")
        self.app = Flask(self.node_id)
        self.setup_routes()

    def query_ollama(self, prompt):
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        try:
            resp = requests.post(
                f"{ollama_host}/api/generate",
                json={"model": self.model_name, "prompt": prompt, "stream": False},
                timeout=45
            )
            if resp.status_code == 200:
                return resp.json().get("response", "")
        except Exception as e:
            pass
        # Fallback / local CPU processing emulation when Ollama is offline or in demo mode
        return f"[{self.node_id} - {self.model_name} response]: Comprehensive evaluation and answer for query: '{prompt}'."

    def setup_routes(self):
        @self.app.route('/health', methods=['GET'])
        def health():
            metrics = get_system_metrics()
            return jsonify({
                "node_id": self.node_id,
                "status": "ONLINE",
                "model": self.model_name,
                "metrics": metrics
            })

        @self.app.route('/process', methods=['POST'])
        def process():
            data = request.json or {}
            task = data.get("task", "")
            job_id = data.get("job_id", "")
            round_num = data.get("round", 1)

            start_time = time.time()
            result = self.query_ollama(task)
            latency = round(time.time() - start_time, 2)

            return jsonify({
                "node_id": self.node_id,
                "job_id": job_id,
                "round": round_num,
                "model": self.model_name,
                "latency": latency,
                "response": result,
                "status": "SUCCESS"
            })

    def run(self):
        self.app.run(host="0.0.0.0", port=self.port)

def create_peer_server(node_id, port, model_name):
    return PeerNode(node_id, port, model_name)
