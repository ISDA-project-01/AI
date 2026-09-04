@echo off
TITLE VAPIC PC4 AI Peer Node Setup
echo ====================================================
echo      VAPIC - PC4 PEER NODE SETUP (Llama)
echo ====================================================

call ..\venv\Scripts\activate.bat 2>nul || python -m venv venv && call venv\Scripts\activate.bat
pip install -r ..\requirements.txt

set NODE_PORT=8003
set NODE_MODEL=llama3.2:3b
echo Starting PC4 Node Server on port %NODE_PORT% with model %NODE_MODEL%...
python ..\node3.py
pause
