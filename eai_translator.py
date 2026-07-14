import os
import json
import time
import threading
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini AI (if key is provided)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
translated_alerts = []

def generate_fallback_translation(signature):
    """
    Fallback Heuristics: Used if the Gemini API key is missing or the API rate limits.
    """
    sig_upper = signature.upper()
    if any(k in sig_upper for k in ["MALWARE", "TROJAN", "COINMINER", "RANSOMWARE", "BACKDOOR"]):
        return {"severity": "Critical", "explanation": "Malicious software detected attempting to communicate.", "action": "Isolate the machine."}
    elif any(k in sig_upper for k in ["EXPLOIT", "CVE-", "SHELLCODE"]):
        return {"severity": "High", "explanation": "Attacker attempting to exploit a known vulnerability.", "action": "Verify patches and block IP."}
    elif any(k in sig_upper for k in ["SCAN", "PROBE", "NMAP"]):
        return {"severity": "Medium", "explanation": "External device scanning your network for open ports.", "action": "Block unauthorized inbound traffic."}
    else:
        return {"severity": "Low", "explanation": "An unusual network pattern was detected.", "action": "Monitor for further activity."}

def generate_ai_translation(signature, src_ip, dest_ip):
    """
    True eAI Engine: Queries Google's Gemini LLM to dynamically translate the signature.
    """
    if not GEMINI_API_KEY:
        return generate_fallback_translation(signature)
        
    prompt = f"""
    You are an expert cybersecurity analyst. A Suricata Intrusion Detection System just flagged the following technical signature on a small business's network:
    
    Signature: {signature}
    Source IP: {src_ip}
    Destination IP: {dest_ip}
    
    Translate this threat into plain, simple English for a non-technical business owner. 
    You must respond ONLY with a raw JSON object in the exact following format, without any markdown formatting or backticks:
    {{
        "severity": "Critical/High/Medium/Low",
        "explanation": "A 1-2 sentence plain-English explanation of what this threat means.",
        "action": "A 1-sentence simple instruction on what the business owner should do."
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # Clean up possible markdown code blocks from LLM response
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
            
        return json.loads(text.strip())
    except Exception as e:
        print(f"[eAI ERROR] Gemini API failed ({e}). Using fallback heuristics.")
        return generate_fallback_translation(signature)

def translate_suricata_alert(alert_data):
    """
    Parses the raw JSON and applies the eAI translation.
    """
    signature = alert_data.get('alert', {}).get('signature', 'Unknown Signature')
    src_ip = alert_data.get('src_ip', 'Unknown')
    dest_ip = alert_data.get('dest_ip', 'Unknown')
    timestamp = alert_data.get('timestamp', 'Unknown Time')

    eai_intel = generate_ai_translation(signature, src_ip, dest_ip)

    return {
        "timestamp": timestamp,
        "source_ip": src_ip,
        "target_ip": dest_ip,
        "technical_signature": signature,
        "severity": eai_intel.get("severity", "Medium"),
        "plain_english_explanation": eai_intel.get("explanation", "Threat detected."),
        "recommended_action": eai_intel.get("action", "Monitor network.")
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
                    print(f"[eAI TRANSLATED] Real Threat Detected: {translated['technical_signature']}")
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
    print("Starting eAI-Translator Dashboard on port 8080...")
    # Bind to 0.0.0.0 so it is accessible when running inside Docker
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
