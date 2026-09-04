import os
from peer_base import create_peer_server

if __name__ == "__main__":
    port = int(os.getenv("NODE_PORT", 8001))
    model = os.getenv("NODE_MODEL", "qwen2.5-coder:3b")
    node = create_peer_server("pc2", port, model)
    print(f"Starting PC2 Node Server on port {port} with model {model}...")
    node.run()
