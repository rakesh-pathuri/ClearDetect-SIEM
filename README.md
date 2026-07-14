# ClearDetect SIEM

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Architecture-Docker-2496ED)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Core Goal:** The ultimate objective of this project is to make enterprise-grade cybersecurity stupid-simple. By combining a one-click deployment architecture with an Explainable AI (eAI) translation layer, this tool enables non-technical small and medium business owners to actively monitor their networks without needing a dedicated cybersecurity team.

## Overview

In traditional cybersecurity, enterprise tools like Security Information and Event Management (SIEM) systems output highly complex, technical logs. Understanding these logs usually requires a dedicated, full-time cybersecurity team, which leaves small businesses unprotected.

This project solves that gap. Instead of building a new Intrusion Detection System from scratch, it leverages **Suricata** (an industry-standard threat engine) and layers a custom **Explainable AI (eAI)** translation pipeline on top of it. When Suricata flags a packet, the eAI engine intercepts the technical alert, translates it into plain English, and provides immediate, actionable remediation steps for the business owner via a clean web dashboard.

## Project Architecture

The repository contains three main components working together in a unified Docker architecture:

1. **Suricata Network Sensor**: 
   - Sits at the network edge and sniffs incoming traffic.
   - Outputs highly technical JSON telemetry alerts (`eve.json`) when it detects malicious signatures.
2. **eAI Translator (`eai_translator.py`)**: 
   - A Python microservice that continuously monitors the Suricata log file in real-time.
   - Extracts technical metadata (e.g., `ET EXPLOIT Possible CVE-2021-44228`) and passes it through an NLP heuristic pipeline to generate human-readable explanations.
3. **SIEM Dashboard**: 
   - A dark-theme, Kibana-inspired web interface built with Flask and plain JavaScript. 
   - Subscribes to the eAI Translator to stream translated cyber alerts live to the browser.

## Technologies Used

- **Network Security**: Suricata IDS
- **Orchestration**: Docker, Docker Compose
- **Web Framework**: Python Flask
- **Frontend**: HTML5, CSS, Vanilla JavaScript

## How to Run Locally

### Prerequisites
Make sure you have `Docker Desktop` and `git` installed on your machine.

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakesh-pathuri/ClearDetect-SIEM.git
   cd ClearDetect-SIEM
   ```

2. **Deploy the Architecture:**
   *ClearDetect is built for absolute simplicity. Deploy the entire orchestrated stack with a single command:*
   ```bash
   docker compose up --build -d
   ```

3. **Access the Dashboard:**
   Open your web browser and navigate to **`http://localhost:8080`**.

### Testing the System

To verify that the Suricata sensor is actively sniffing traffic and the eAI engine is translating it, you can trigger a live alert.

1. **Run the Test Script:**
   Open a terminal and run the provided test batch file:
   ```bash
   test_alert.bat
   ```

   *This script forces the Suricata Docker container to ping a known malicious test URL (`testmyids.com`). You will instantly see the resulting translated alert populate on your Live Threat Stream dashboard.*

---

### Authorship
**Developed by:** Rakesh Pathuri
*Architected to democratize enterprise-grade network security, empowering small businesses with clear, actionable threat intelligence.*
