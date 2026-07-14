# ClearDetect SIEM: Enterprise Suricata Orchestration

[![Suricata IDS](https://img.shields.io/badge/Sensor-Suricata-red)](https://suricata.io/)
[![Python 3.11](https://img.shields.io/badge/Brain-Python_3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED)](https://www.docker.com/)

> **Development Context:** This is a production-grade Security Information and Event Management (SIEM) system built for Small and Medium Businesses (SMBs). It integrates an industry-standard Intrusion Detection System (Suricata) with a dynamic Explainable AI (eAI) engine, transforming dense network telemetry into actionable security intelligence.

## 📖 Overview

Standard SIEMs output highly dense, technical JSON logs when they detect an anomaly (e.g., `ET EXPLOIT Possible CVE-2014-6271 Attempt in Headers`). A small business owner without a dedicated Security Operations Center (SOC) cannot decipher these alerts, leading to alert fatigue and ignored threats.

This project wraps **Real Suricata** in a Docker container and attaches a **Python Explainable AI (eAI) Engine** to its output stream. The eAI Engine intercepts the dense JSON alerts in real-time, applies dynamic Natural Language Processing (NLP) heuristics, and translates the threat into a plain-English explanation displayed on a hardcore, high-density SIEM dashboard.

## 🏗️ Architecture

- **Suricata Sensor (`jasonish/suricata`)**: The actual open-source IDS engine. It sniffs network traffic and outputs alerts to a volume-mapped `eve.json` file. It automatically pulls the latest Emerging Threats (ET) ruleset on boot.
- **eAI Translator Engine (`xai_translator.py`)**: A Python microservice that tails the real `eve.json` file, intercepts alerts, and translates them dynamically.
- **SIEM Web Dashboard**: A high-density, dark-mode enterprise UI built with HTML/CSS and served via Flask.

## 🚀 Deployment (Requires WSL/Docker)

To run this real enterprise stack on Windows, you **must** have Docker Desktop and WSL (Windows Subsystem for Linux) installed.

1. **Install WSL (If not already installed):**
   Run an administrative PowerShell and type:
   ```bash
   wsl --install
   ```
   *Restart your computer after this completes.*

2. **Deploy the Enterprise Stack:**
   Ensure Docker Desktop is running, then execute:
   ```bash
   docker compose up --build -d
   ```

3. **View the SIEM Console:**
   Open your browser to: **[http://localhost:8080](http://localhost:8080)**

## 🕵️‍♂️ How to Test the IDS

To prove the system works, we will use the industry-standard method of intentionally triggering a real Suricata signature.

Run the provided batch script:
```cmd
test_alert.bat
```
*(Or manually run: `docker exec suricata-sensor curl -s http://testmyids.com`)*

This sends a specific packet over the network that matches a known malware signature. Suricata will physically catch it, the Python engine will translate it, and you will see the real threat pop up on your dashboard instantly!
