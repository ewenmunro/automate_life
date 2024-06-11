import logging
import time
import os
from datetime import datetime

# configure logging
logging.basicConfig(filename='stand_up_notification.log', level=logging.INFO)

# Initialize the timer
last_alert_time = 0
last_activity_time = time.time()

while True:
    # Check if the user is logged in
    is_logged_in = os.popen('pgrep -x "loginwindow"').read().strip() != ''

    if is_logged_in:
        current_time = time.time()
        elapsed_time = current_time - last_alert_time

        # Check for inactivity
        inactive_time = current_time - last_activity_time

        if elapsed_time >= 3600 or inactive_time >= 3600:
            # Send a notification
            logging.info('Sending notification to stand up and move around')
            os.system("""
                      osascript -e 'display notification "Get off your butt!" with title "Stand Up Notification"'
                      """)
            os.system('afplay /System/Library/Sounds/Glass.aiff')
            print('Sent notification at',
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Calculate the elapsed time in hours, minutes, and seconds
            elapsed_time = datetime.utcfromtimestamp(
                current_time - last_alert_time)
            elapsed_time_str = elapsed_time.strftime('%H:%M:%S')
            print('Elapsed time since last alert:', elapsed_time_str)

            # Save the current time as the last alert time
            last_alert_time = current_time
            print('Updated last alert time to',
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # Reset the inactivity timer
            last_activity_time = current_time

        # Wait for the remaining time in the hour before checking again
        elapsed_time_seconds = round(current_time - last_alert_time)
        inactive_time_seconds = round(current_time - last_activity_time)
        if elapsed_time_seconds >= 3600 or inactive_time_seconds >= 3600:
            remaining_time = 3600
        else:
            remaining_time = 3600 - \
                max(elapsed_time_seconds, inactive_time_seconds)
        remaining_time_str = datetime.utcfromtimestamp(remaining_time)
        remaining_time_str = remaining_time_str.strftime('%H:%M:%S')
        print('Remaining time in hour:', remaining_time_str)
        time.sleep(60)
        print('Checked at', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        # Reset the timer if the user is not logged in
        last_alert_time = 0
        last_activity_time = time.time()

        # Wait for a minute before checking again
        time.sleep(60)
        print('Checked at', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
