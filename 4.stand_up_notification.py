import logging
import time
import os
from datetime import datetime

# configure logging
logging.basicConfig(filename='stand_up_notification.log', level=logging.INFO)

# Initialize the timer
last_alert_time = 0

while True:
    # Check if the user is logged in
    is_logged_in = os.popen('pgrep -x "loginwindow"').read().strip() != ''

    if is_logged_in:
        current_time = time.time()
        elapsed_time = current_time - last_alert_time

        if elapsed_time >= 3600:
            # Send a notification
            logging.info('Sending notification to stand up and move around')
            os.system("""
                      osascript -e 'display notification "Get off your butt!" with title "Stand Up Notification"'
                      """)
            os.system('afplay /System/Library/Sounds/Glass.aiff')
            print('Sent notification at',
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Save the current time as the last alert time
            last_alert_time = current_time
            print('Updated last alert time to',
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Calculate the elapsed time in hours, minutes, and seconds
        elapsed_time = datetime.utcfromtimestamp(
            current_time - last_alert_time)
        elapsed_time_str = elapsed_time.strftime('%H:%M:%S')
        print('Elapsed time since last alert:', elapsed_time_str)

        # Wait for the remaining time in the hour before checking again
        elapsed_time_seconds = round(current_time - last_alert_time)
        remaining_time = 3600 - elapsed_time_seconds % 3600
        remaining_time_str = datetime.utcfromtimestamp(remaining_time)
        remaining_time_str = remaining_time_str.strftime('%H:%M:%S')
        print('Remaining time in hour:', remaining_time_str)
        time.sleep(remaining_time)
        print('Checked at', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        # Reset the timer if the user is not logged in
        last_alert_time = 0

        # Wait for a minute before checking again
        time.sleep(60)
        print('Checked at', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
