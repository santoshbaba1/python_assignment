import psutil
import time

THRESHOLD = 80  # CPU usage limit (%)

try:
    print("Monitoring CPU usage... (Press Ctrl+C to stop)\n")

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)

        if cpu_usage > THRESHOLD:
            print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")
        else:
            print(f"CPU usage: {cpu_usage}%")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

except Exception as e:
    print(f"Error occurred: {e}")
