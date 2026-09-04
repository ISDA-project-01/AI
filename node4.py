import os
from peer_base import create_peer_server

if __name__ == "__main__":
    port = int(os.getenv("NODE_PORT", 8004))
    model = os.getenv("NODE_MODEL", "deepseek-r1:1.5b")
    node = create_peer_server("pc5", port, model)
    print(f"Starting PC5 Node Server on port {port} with model {model}...")
    node.run()
