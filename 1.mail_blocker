import subprocess
import datetime
import time
import sys

# Redirect stdout to log file
sys.stdout = open('mail_blocker.log', 'a')

print("Starting mail blocker...")

allowed_start_time = datetime.time(17, 0, 0) # 5pm
allowed_end_time = datetime.time(23, 0, 0) # 11pm

while True:
    current_time = datetime.datetime.now()
    hour = current_time.time().hour
    print(f"Current hour: {hour}")
    print(f"Allowed start time: {allowed_start_time}")
    print(f"Allowed end time: {allowed_end_time}")
    
    if hour >= allowed_start_time.hour and hour <= allowed_end_time.hour:
        print("Mail app can be used.")
        time.sleep(60)
    else:
        print("Mail app is blocked.")
        subprocess.run(['killall', 'Mail'])
        time.sleep(60)

    sys.stdout.flush()
