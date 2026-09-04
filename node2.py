import os
from peer_base import create_peer_server

if __name__ == "__main__":
    port = int(os.getenv("NODE_PORT", 8002))
    model = os.getenv("NODE_MODEL", "gemma2:2b")
    node = create_peer_server("pc3", port, model)
    print(f"Starting PC3 Node Server on port {port} with model {model}...")
    node.run()
