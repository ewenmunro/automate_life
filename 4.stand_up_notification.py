import time
import os

# Save the current time when the script starts running
last_alert_time = time.time()

while True:
    # Check if an hour has passed since the last alert
    current_time = time.time()
    if current_time - last_alert_time >= 3600:
        # Send a notification
        os.system("""
                  osascript -e 'display notification "Get off your butt!" with title "Time to Move" sound name "default" '
                  """)
        # Save the current time as the last alert time
        last_alert_time = current_time
    
    # Wait for a minute before checking again
    time.sleep(60)
