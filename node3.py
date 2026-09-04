import os
from peer_base import create_peer_server

if __name__ == "__main__":
    port = int(os.getenv("NODE_PORT", 8003))
    model = os.getenv("NODE_MODEL", "llama3.2:3b")
    node = create_peer_server("pc4", port, model)
    print(f"Starting PC4 Node Server on port {port} with model {model}...")
    node.run()
