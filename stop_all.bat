@echo off
TITLE VAPIC Cluster Control - Stop All
echo Stopping all VAPIC Python processes...
taskkill /FI "WINDOWTITLE eq VAPIC*" /F /T 2>nul
taskkill /IM python.exe /F 2>nul
echo All cluster processes terminated.
pause
