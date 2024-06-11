import psutil
import subprocess
import time

# Battery percentage thresholds
low_threshold = 10
high_threshold = 100


def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent if battery else None
    return percent


def play_sound():
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])


def main():
    sound_played = False  # Flag to track if sound has been played

    while True:
        battery_percent = check_battery()

        if battery_percent is not None:
            if battery_percent <= low_threshold and not sound_played:
                print(
                    f"Battery level is {battery_percent}% or lower. Playing sound.")
                play_sound()
                sound_played = True  # Set flag to True after playing sound
            elif battery_percent >= high_threshold and not sound_played:
                print(
                    f"Battery level is {battery_percent}%. Fully charged. Playing sound.")
                play_sound()
                sound_played = True  # Set flag to True after playing sound

        time.sleep(60)  # Check battery level every 60 seconds


if __name__ == "__main__":
    main()
