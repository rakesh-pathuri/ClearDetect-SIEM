# ClearDetect SIEM

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Architecture-Docker-2496ED)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Core Goal:** The ultimate objective of this project is to make enterprise-grade security stupid-simple. By combining a simple setup architecture with an Explainable AI (eAI) translation layer, this tool enables non-technical small and medium business owners to actively monitor their networks without needing a dedicated technical team.

## Overview

In traditional security, enterprise tools like Security Information and Event Management (SIEM) systems output highly complex, technical logs. Understanding these logs usually requires a dedicated, full-time security team, which leaves small businesses unprotected.

This project solves that gap. Instead of building a new Intrusion Detection System from scratch, it leverages **Suricata** (an industry-standard threat engine) and layers a custom **Explainable AI (eAI)** translation pipeline on top of it. When Suricata flags a packet, the eAI engine intercepts the technical alert, translates it into plain English, and provides immediate, actionable remediation steps for the business owner via a clean web dashboard.

## Project Architecture

The repository contains three main components working together in a unified Docker architecture:

1. **Suricata Network Sensor**: 
   - Sits at the network edge and sniffs incoming traffic.
   - Outputs highly technical JSON telemetry alerts (`eve.json`) when it detects malicious signatures.
2. **eAI Translator (`eai_translator.py`)**: 
   - A Python microservice that continuously monitors the Suricata log file in real-time.
   - Integrating Google's Gemini Large Language Model to dynamically analyze and translate highly technical security alerts into human-readable text.
3. **SIEM Dashboard**: 
   - A dark-theme, Kibana-inspired web interface built with Flask and plain JavaScript. 
   - Subscribes to the eAI Translator to stream translated cyber alerts live to the browser.

## Core Features

- **Suricata Integration**: Powered by an industry-standard, signature-based IDS engine.
- **Generative AI Translation**: Uses Google Gemini to convert complex cyber threats into plain English dynamically.
- **Offline Fallback**: Built-in NLP heuristics guarantee the system continues to work even if the API rate limits or loses connectivity.
- **Simple Deployment**: Entirely Dockerized. No complex configurations or dependency hell.
- **Kibana-Style Dashboard**: A sleek, professional dark-theme SIEM interface designed for ultimate data clarity.

## Technologies Used

- **Network Security Engine**: Suricata IDS
- **Explainable AI Engine**: Google Gemini LLM API (`google-generativeai`)
- **Orchestration**: Docker, Docker Compose
- **Backend Translation Service**: Python `Flask`
- **Frontend Infrastructure**: HTML5, Vanilla CSS, Vanilla JavaScript

## How to Run Locally

### Prerequisites
Make sure you have **Docker Desktop** installed and running on your system. You will also need a free **Google Gemini API Key** (from Google AI Studio).

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakesh-pathuri/ClearDetect-SIEM.git
   cd ClearDetect-SIEM
   ```

2. **Configure API Key:**
   Copy the example environment file and add your Gemini API key:
   ```bash
   cp .env.example .env
   ```
   *Open the `.env` file and replace `your_api_key_here` with your real key.*

3. **Deploy the Architecture:**
   *ClearDetect is built for absolute simplicity. Deploy the orchestrated stack with a simple setup command:*
   ```bash
   docker compose up --build -d
   ```

4. **Access the Dashboard:**
   Open your web browser and navigate to **`http://localhost:8080`**.

### Testing the System

To verify that the Suricata sensor is actively sniffing traffic and the eAI engine is translating it, you can trigger a live alert.

1. **Run the Test Script:**
   Open a terminal and run the provided test batch file:
   ```bash
   test_alert.bat
   ```

   *This script forces the Suricata Docker container to ping a known malicious test URL (`testmyids.com`). You will instantly see the resulting translated alert populate on your Live Threat Stream dashboard.*

### Open Source Credits

The core packet-sniffing engine used in this repository is powered by **Suricata** ([OISF](https://suricata.io/)), a world-class, high-performance, open-source network analysis and threat detection engine. I extend my deepest gratitude to the Open Information Security Foundation and the Suricata community for maintaining such an incredible open-source security tool.

---

### Authorship
**Developed by:** Rakesh Pathuri
*Built to make enterprise security simple and accessible for Small and Medium Enterprises (SMEs).*
