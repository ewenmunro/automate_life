import logging
import time
import os

# configure logging
logging.basicConfig(filename='stand_up_notification.log', level=logging.INFO)

# Initialize the timer
last_alert_time = 0

while True:
    # Check if the computer is awake
    is_awake = os.popen('ioreg -c IODisplayWrangler | grep -i IOPowerManagement').read()
    is_awake = 'PowerManagementAssertion' in is_awake
    
    # If the computer is awake, increment the timer
    if is_awake:
        current_time = time.time()
        elapsed_time = current_time - last_alert_time
        
        # Check if an hour has passed since the last alert
        if elapsed_time >= 3600:
            # Send a notification
            logging.info('Sending notification to stand up and move around')
            os.system("""
                      osascript -e 'display notification "Get off your butt!" sound name "default" '
                      """)
            os.system('afplay /System/Library/Sounds/Glass.aiff')
            print('Sent notification at', time.strftime('%Y-%m-%d %H:%M:%S'))
            
            # Save the current time as the last alert time
            last_alert_time = current_time
            print('Updated last alert time to', time.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        # Reset the timer if the computer is asleep
        last_alert_time = 0
    
    # Wait for a minute before checking again
    time.sleep(60)
    print('Checked at', time.strftime('%Y-%m-%d %H:%M:%S'))
