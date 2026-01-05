# DevOps Automation & Monitoring Using Python

    This repository contains Python scripts demonstrating core DevOps concepts such as security validation, system monitoring, configuration management, and automated backups.

# Project Overview

    The project consists of four independent tasks:
    Password Strength Checker – Ensures secure passwords.
    CPU Health Monitoring – Monitors CPU usage and alerts on high load.
    Configuration File Parser – Parses configuration files, stores data in a database, and exposes it via an API.
    Automated Backup Script – Backs up files with timestamp-based versioning.

# Technologies Used
    
    Python 3.x
    psutil (system monitoring)
    Flask (REST API)
    mongoDB (database)
    
# Standard Python libraries:
    os
    sys
    shutil
    datetime
    configparser
    json
    re

    Project Structure
        -password_checker.py
        -cpu_monitor.py
        -config_parser.py
        -config.ini
        -backup.py
        -config.db
        -README.md


# Q1. Password Strength Checker

Features
    Minimum length of 8 characters
    Must contain:
    Uppercase letters
    Lowercase letters
    Digits (0–9)
    Special characters (!@#$%^&*)

    Run the Script
    python password_checker.py

Sample Output
Strong password! Meets all security requirements.

<img width="952" height="388" alt="password op" src="https://github.com/user-attachments/assets/223ea1a0-5088-47d2-9ec2-184f4d2f9abd" />

# Q2. CPU Health Monitoring
    Features
    Continuous CPU monitoring
    Alert if CPU usage exceeds 80%
    Runs until interrupted
    Handles runtime errors gracefully

    # Install Dependency
    pip install psutil

    # Run the Script
    python cpu_monitor.py

Sample Output
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%

<img width="959" height="391" alt="cpu 1" src="https://github.com/user-attachments/assets/218c2d2d-19bc-445b-977a-7ea86c5ef312" />

<img width="950" height="351" alt="cpu break" src="https://github.com/user-attachments/assets/c931d08f-a0fc-4da3-92e8-254ed919e978" />

<img width="995" height="700" alt="cpr stres test" src="https://github.com/user-attachments/assets/6fded6a3-5466-4ea0-91fe-239b5780c5e5" />

# Q3. Configuration Management Automation
    Features
    Reads .ini configuration files
    Extracts key-value pairs
    Stores configuration as JSON in SQLite database
    Exposes configuration via REST API (GET)
    Error handling

    Sample Configuration File (config.ini)
    [Database]
    host = localhost
    port = 3306
    username = admin
    password = secret

    [Server]
    address = 192.168.0.1
    port = 8080

    Run the Script
    python config_parser.py

    API Endpoint
    GET http://127.0.0.1:5000/config

    Sample API Response
    {
        "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
        },
        "Server": {
        "address": "192.168.0.1",
        "port": "8080"
        }
    }


<img width="956" height="391" alt="config op" src="https://github.com/user-attachments/assets/23676ca0-35a9-49e1-a52f-643caffa4b64" />

# Q4. Automated Backup Script
    Features
    Accepts source and destination directories as arguments
    Copies files securely
    Appends timestamp if file already exists
    Handles missing directories gracefully

    Run the Script
    python backup.py /path/to/source /path/to/destination

<img width="950" height="189" alt="backup op" src="https://github.com/user-attachments/assets/92681d16-35e5-4929-91ef-25eac18d5340" />

# Author
Santosh Kumar Sharma
12394
