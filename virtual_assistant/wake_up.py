# libraries
import speech_recognition as sr
import subprocess
import os
import datetime
import time


# start running script
def start_program():
    print("Starting script...")
    script_path = os.path.abspath('virtual_assistant.py')
    subprocess.Popen(['python3', script_path])


# voice recognition
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except:
            print("Sorry, could not recognize your voice.")
            return ""


#  main function
def main():
    while True:
        text = get_audio().lower()

        if "wake up" in text:
            start_program()

        now = datetime.datetime.now()
        if now.hour == 7 and now.minute == 0:
            start_program()

        time.sleep(1)


# execute main function
if __name__ == '__main__':
    main()


# to run the program in the background, type in the terminal 'nohup python3 wake_up.py > wake_up.log 2>&1 &'
