@echo off
TITLE VAPIC Cluster Control - Start All
echo Starting VAPIC Local Cluster Simulation...

start "PC1 Master API" cmd /k "python api.py"
start "PC2 Node (Qwen)" cmd /k "set NODE_PORT=8001 && set NODE_MODEL=qwen2.5-coder:3b && python node1.py"
start "PC3 Node (Gemma)" cmd /k "set NODE_PORT=8002 && set NODE_MODEL=gemma2:2b && python node2.py"
start "PC4 Node (Llama)" cmd /k "set NODE_PORT=8003 && set NODE_MODEL=llama3.2:3b && python node3.py"
start "PC5 Node (DeepSeek)" cmd /k "set NODE_PORT=8004 && set NODE_MODEL=deepseek-r1:1.5b && python node4.py"

echo All 5 nodes started in separate windows.
