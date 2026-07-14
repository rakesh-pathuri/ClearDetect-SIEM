from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Hardcoded alerts just for viewing the UI design
SAMPLE_ALERTS = [
    {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source_ip": "185.15.59.2",
        "target_ip": "10.0.0.5",
        "technical_signature": "ET EXPLOIT Possible CVE-2021-44228 Apache Log4j RCE Attempt",
        "severity": "Critical",
        "plain_english_explanation": "An attacker is attempting to exploit a known software vulnerability to gain unauthorized access to your systems.",
        "recommended_action": "Verify that all servers are fully updated with the latest security patches. Block the Source IP."
    },
    {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source_ip": "203.0.113.42",
        "target_ip": "192.168.1.50",
        "technical_signature": "ET MALWARE Win32/CoinMiner Mac OS X Miner",
        "severity": "High",
        "plain_english_explanation": "Malicious software designed to hijack your computer's processing power was detected.",
        "recommended_action": "Run a full antivirus scan on the destination computer immediately."
    },
    {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source_ip": "192.168.1.105",
        "target_ip": "10.0.0.1",
        "technical_signature": "ET SCAN Nmap OS Detection Probe",
        "severity": "Medium",
        "plain_english_explanation": "An external device is actively scanning your network to map out open ports and identify vulnerabilities.",
        "recommended_action": "If the Source IP is not a known IT administrator, ensure your firewall is configured to block unauthorized inbound traffic."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/alerts')
def get_alerts():
    return jsonify(SAMPLE_ALERTS)

if __name__ == '__main__':
    print("[*] Running Temporary UI Viewer for Portfolio Screenshots...")
    app.run(host='0.0.0.0', port=8080, debug=False)
