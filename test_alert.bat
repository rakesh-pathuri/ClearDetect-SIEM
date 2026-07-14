@echo off
echo [*] Sending malicious signature to trigger Real Suricata IDS...
echo.
docker exec suricata-sensor curl -s http://testmyids.com
echo.
echo [*] Trigger sent! Check your XAI Dashboard at http://localhost:8080 to see the real translation!
pause
