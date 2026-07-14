# ClearDetect SIEM

ClearDetect SIEM is a Security Information and Event Management tool designed specifically for Small and Medium Businesses. It uses a real Intrusion Detection System (Suricata) to monitor network traffic for cyber threats. 

Most enterprise security tools output highly technical logs that require a dedicated cybersecurity team to understand. ClearDetect solves this problem by using an Explainable AI translation engine. When Suricata detects a network threat, the engine translates the complex technical signature into plain English and provides a clear, actionable recommendation for the business owner.

## Architecture

The system consists of three main components:

1. Suricata Sensor: A Docker container that monitors network traffic and outputs technical alerts to a log file.
2. Translation Engine (`eai_translator.py`): A Python service that constantly monitors the Suricata logs, intercepts new alerts, and translates them into plain English.
3. SIEM Dashboard: A professional, dark-theme web interface that displays the translated alerts in real-time.

## Deployment Instructions

To run this tool, you must have Docker Desktop and Windows Subsystem for Linux (WSL) installed.

1. Ensure Docker Desktop is running in the background.
2. Open a terminal in the project directory.
3. Run the following command to build and start the system:
   
   docker compose up --build -d

4. Open a web browser and navigate to http://localhost:8080.

## Testing the System

To verify the system is working, you can trigger a test alert.
Run the provided test script:

test_alert.bat

This script will send a simulated malicious packet across the network. Suricata will detect it, the Python engine will translate it, and the alert will immediately appear on your dashboard.
