# ClearDetect SIEM

ClearDetect SIEM is a Security Information and Event Management tool designed specifically for Small and Medium Businesses (SMBs) and non-technical users. 

The goal of this project is to make enterprise-grade cybersecurity stupid-simple. Most security tools output highly complex, technical logs that require a dedicated cybersecurity team to understand. ClearDetect solves this problem by using an Explainable AI (eAI) translation engine that converts complex network alerts into plain English with clear, actionable recommendations.

## Project Scope and Context

It is important to note that this project did not build a new Intrusion Detection System (IDS) from scratch. Building a reliable IDS requires years of dedicated research and signature development. 

Instead, this project leverages **Suricata**, an industry-standard, open-source threat detection engine. Our core contribution is the architecture built around Suricata:
1. The Explainable AI translation layer that makes the logs readable.
2. The custom, dark-theme web dashboard.
3. A true "one-click" deployment architecture using Docker.

## Architecture

The system consists of three main components:

1. Suricata Sensor: A Dockerized network sensor that sniffs incoming traffic and outputs technical alerts to a JSON log file.
2. eAI Translation Engine: A Python microservice (`eai_translator.py`) that constantly monitors the Suricata logs, intercepts new alerts in real-time, and translates the technical signatures into plain English.
3. SIEM Dashboard: A web-based interface that displays the translated alerts in a clean, professional dark theme (accessible via web browser).

## One-Click Deployment

ClearDetect is designed for absolute simplicity. To deploy the entire SIEM stack, you must have Docker Desktop installed.

1. Clone this repository to your machine.
2. Open a terminal in the project directory.
3. Run the following command:

   docker compose up --build -d

The system will automatically download the Suricata engine, update the latest threat signatures, start the Python translation service, and launch the web server. 

## Usage and Testing

Once the Docker containers are running:
1. Open a web browser and navigate to http://localhost:8080. You will see the Live Threat Stream dashboard.
2. To verify the system is working, run the provided test script:
   
   test_alert.bat

This script sends a simulated malicious packet across your local network. The Suricata sensor will detect it, the Python engine will translate it, and the plain-English alert will instantly appear on your dashboard.
