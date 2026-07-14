# ClearDetect SIEM

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Architecture-Docker-2496ED)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract

Enterprise cybersecurity tools like Security Information and Event Management (SIEM) systems generate highly technical logs that require dedicated security teams to understand. This leaves Small and Medium Businesses (SMBs) without effective threat monitoring. 

**ClearDetect SIEM** solves this problem by integrating a real Intrusion Detection System with an **Explainable AI (eAI)** translation layer. When a threat is detected on the network, the complex technical signature is automatically intercepted, parsed, and translated into plain English, providing business owners with an immediate, non-technical understanding of the threat and actionable remediation steps.

## Important Note on the Architecture

**This project did not build a new Intrusion Detection System from scratch.** Building a reliable IDS requires years of dedicated research, kernel-level packet inspection, and continuous signature development. 

Instead, this project leverages **Suricata**, an industry-standard, battle-tested open-source threat detection engine. The core engineering contribution of this project is the architecture built around Suricata: the real-time Explainable AI translation pipeline, the dark-theme Kibana-style dashboard, and the zero-configuration "one-click" Docker deployment.

## The Explainable AI (eAI) Engine

The core feature of this tool is the **eAI Translator Service** (`eai_translator.py`). 
- **What it does:** The engine actively monitors the highly complex, nested JSON log outputs produced by the Suricata network sensor (`eve.json`).
- **How we use it:** As soon as Suricata flags a packet, the eAI engine intercepts the event in real-time, extracts the technical metadata (like `ET EXPLOIT Possible CVE-2021-44228`), and maps it through a heuristic NLP pipeline. The result is a plain-English explanation of the attack and a clear, immediate action for the user to take. 

## Technical Domains

This project bridges the gap between network security and modern artificial intelligence, utilizing the following domains:

1. **Network Security & Packet Analysis:** Integrating and deploying enterprise-grade Intrusion Detection Systems (Suricata) for real-time packet sniffing and threat identification.
2. **Explainable AI (eAI) & NLP:** Developing heuristic translation pipelines to convert highly technical cybersecurity alerts into human-readable text.
3. **DevOps & Containerization:** Engineering a robust, multi-container orchestration architecture using Docker to ensure absolute cross-platform consistency and one-click deployment.

## Core Features

- **Suricata Integration**: Powered by an industry-standard, signature-based IDS engine.
- **eAI Translation Pipeline**: Converts complex cyber threats into plain English in milliseconds.
- **One-Click Deployment**: Entirely Dockerized. No complex configurations or dependency hell.
- **Kibana-Style Dashboard**: A sleek, professional dark-theme SIEM interface designed for ultimate data clarity.

## Technical Stack

- **Network Security Engine**: Suricata IDS
- **Orchestration**: Docker, Docker Compose
- **Backend Translation Engine**: Python `Flask`
- **Frontend Infrastructure**: HTML5, Vanilla CSS, Vanilla JavaScript

## Installation & Usage

### Prerequisites
Make sure you have **Docker Desktop** installed and running on your system. 

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakesh-pathuri/ClearDetect-SIEM.git
   cd ClearDetect-SIEM
   ```

2. **Deploy the System:**
   *ClearDetect is designed for absolute simplicity. Run one command to deploy the entire stack.*
   ```bash
   docker compose up --build -d
   ```

3. **Access the Dashboard:**
   Open your web browser and navigate to:
   **`http://localhost:8080`**

### Testing the System

To verify the system is actively sniffing your network, run the provided test script in your terminal:
```bash
test_alert.bat
```
*This script sends a simulated malicious packet across your local network. The Dockerized Suricata sensor will detect it, the Python eAI engine will translate it, and the plain-English alert will instantly appear on your Live Threat Stream dashboard.*

---
### Authorship & Contributions

**Lead Developer & Primary Author:** Rakesh Pathuri

*The entirety of this project's software architecture, the eAI translation pipeline, the Docker orchestration, and the web infrastructure within this repository were independently designed and built by Rakesh Pathuri.*
