# Suricata XAI: Explainable Security for SMBs

[![Suricata IDS](https://img.shields.io/badge/Sensor-Suricata-red)](https://suricata.io/)
[![Python 3.11](https://img.shields.io/badge/Brain-Python_3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED)](https://www.docker.com/)

> **Development Context:** This is an enterprise-grade cybersecurity thesis project designed to integrate Explainable AI (XAI) with an industry-standard Intrusion Detection System (IDS). It solves the problem of "alert fatigue" by translating complex network signatures into actionable, plain-English advice tailored for Small and Medium Businesses (SMBs).

## 📖 Overview

Standard Intrusion Detection Systems (like Suricata) output highly dense, technical JSON logs when they detect an anomaly (e.g., `ET EXPLOIT Possible CVE-2014-6271 Attempt in Headers`). A small business owner without a dedicated Security Operations Center (SOC) cannot decipher these alerts, leading to alert fatigue and ignored threats.

This project wraps **Real Suricata** in a Docker container and attaches a **Python XAI-Translator Engine** to its output stream. The XAI Engine intercepts the dense JSON alerts in real-time, applies dynamic Natural Language Processing (NLP) heuristics, and translates the threat into a plain-English explanation displayed on a beautiful SOC dashboard.

## 🏗️ Architecture

- **Suricata Sensor (`jasonish/suricata`)**: The actual open-source IDS engine. It sniffs network traffic and outputs alerts to a volume-mapped `eve.json` file. It automatically pulls the latest Emerging Threats (ET) ruleset on boot.
- **XAI Translator Engine (`xai_translator.py`)**: A Python microservice that tails the real `eve.json` file, intercepts alerts, and translates them dynamically.
- **SOC Web Dashboard**: A high-density, enterprise-grade dark-mode UI built with HTML/CSS and served via Flask.

## 🚀 How to Run (One-Click Deployment)

Because this relies on real network sniffing and microservice orchestration, the entire stack is packaged using Docker Compose.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakesh-pathuri/Suricata-XAI-IDS.git
   cd Suricata-XAI-IDS
   ```

2. **Deploy the Enterprise Stack:**
   Ensure Docker Desktop is running, then execute:
   ```bash
   docker-compose up --build -d
   ```
   *This command pulls the real Suricata engine, builds the Python XAI container, maps the logs, and starts both services in the background.*

3. **View the SOC Dashboard:**
   Open your browser to: **[http://localhost:8080](http://localhost:8080)**

## 🕵️‍♂️ How to Test the IDS

To prove the system works, we will use the industry-standard method of intentionally triggering a real Suricata signature.

Run the provided batch script:
```cmd
test_alert.bat
```
*(Or manually run: `docker exec suricata-sensor curl -s http://testmyids.com`)*

This sends a specific packet over the network that matches a known malware signature. Suricata will physically catch it, the Python engine will translate it, and you will see the real threat pop up on your dashboard instantly!

---

### Authorship
**Developed by:** Rakesh Pathuri
*Built to bridge the gap between enterprise Intrusion Detection Systems and non-technical business owners using Explainable AI heuristics.*
