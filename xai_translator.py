import os
import json
import time
import threading
from flask import Flask, render_template, jsonify

app = Flask(__name__)
translated_alerts = []

def generate_heuristic_translation(signature):
    """
    XAI Engine: Uses NLP heuristics to translate ANY technical Suricata signature 
    into a plain-English, actionable explanation for SMB owners.
    """
    sig_upper = signature.upper()
    
    if any(keyword in sig_upper for keyword in ["MALWARE", "TROJAN", "COINMINER", "RANSOMWARE", "BACKDOOR"]):
        return {
            "severity": "Critical",
            "explanation": "Malicious software (Malware/Trojan) has been detected attempting to communicate or execute on your network. This could lead to data theft or system damage.",
            "action": "Isolate the affected machine (Target IP) from the network immediately and run a full enterprise antivirus scan."
        }
    elif any(keyword in sig_upper for keyword in ["EXPLOIT", "CVE-", "SHELLCODE"]):
        return {
            "severity": "High",
            "explanation": "An attacker is attempting to exploit a known software vulnerability to gain unauthorized access to your systems.",
            "action": "Verify that all servers and applications are fully updated with the latest security patches. Block the Source IP."
        }
    elif any(keyword in sig_upper for keyword in ["SCAN", "PROBE", "NMAP"]):
        return {
            "severity": "Medium",
            "explanation": "An external device is actively scanning your network to map out open ports and identify vulnerabilities. This is often reconnaissance before an attack.",
            "action": "If the Source IP is not a known IT administrator, ensure your firewall is configured to block unauthorized inbound traffic from it."
        }
    elif any(keyword in sig_upper for keyword in ["POLICY", "INFO", "LEAK"]):
        return {
            "severity": "Low",
            "explanation": "Traffic matching a corporate policy violation or potential information leak was detected.",
            "action": "Review the internal endpoint's activity to ensure no sensitive data is being transmitted insecurely."
        }
    else:
        return {
            "severity": "Medium",
            "explanation": "An unusual network pattern was detected that violates standard security rules.",
            "action": "Monitor the Source IP for further suspicious activity."
        }

def translate_suricata_alert(alert_data):
    """
    Parses the raw JSON and applies the XAI translation.
    """
    signature = alert_data.get('alert', {}).get('signature', 'Unknown Signature')
    src_ip = alert_data.get('src_ip', 'Unknown')
    dest_ip = alert_data.get('dest_ip', 'Unknown')
    timestamp = alert_data.get('timestamp', 'Unknown Time')

    xai_intel = generate_heuristic_translation(signature)

    return {
        "timestamp": timestamp,
        "source_ip": src_ip,
        "target_ip": dest_ip,
        "technical_signature": signature,
        "severity": xai_intel["severity"],
        "plain_english_explanation": xai_intel["explanation"],
        "recommended_action": xai_intel["action"]
    }

def tail_suricata_logs():
    """
    Continuously monitors the REAL Suricata eve.json log file for new alerts.
    """
    log_file = "logs/eve.json"
    
    # Ensure directory exists, wait for Suricata to create the file
    os.makedirs("logs", exist_ok=True)
    
    print(f"Waiting for Suricata to initialize {log_file}...")
    while not os.path.exists(log_file):
        time.sleep(2)
        
    print(f"Started monitoring {log_file} for real intrusion alerts...")
    
    with open(log_file, 'r') as f:
        # Move to the end of file so we only see NEW alerts
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
                
            try:
                data = json.loads(line)
                # We only care about intrusion alerts
                if data.get("event_type") == "alert":
                    translated = translate_suricata_alert(data)
                    translated_alerts.insert(0, translated)
                    if len(translated_alerts) > 50:
                        translated_alerts.pop()
                    print(f"[XAI TRANSLATED] Real Threat Detected: {translated['technical_signature']}")
            except json.JSONDecodeError:
                pass

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/alerts')
def get_alerts():
    return jsonify(translated_alerts)

if __name__ == '__main__':
    threading.Thread(target=tail_suricata_logs, daemon=True).start()
    print("Starting XAI-Translator Dashboard on port 8080...")
    # Bind to 0.0.0.0 so it is accessible when running inside Docker
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
