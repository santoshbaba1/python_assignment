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

# Q4. Automated Backup Script
    Features
    Accepts source and destination directories as arguments
    Copies files securely
    Appends timestamp if file already exists
    Handles missing directories gracefully

    Run the Script
    python backup.py /path/to/source /path/to/destination

# Author
Santosh Kumar Sharma
12394