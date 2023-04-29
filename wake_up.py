# libraries
import speech_recognition as sr
import subprocess
import os


# start running script
def start_program():
    print("Starting script...")
    # insert program to run    
    script_path = os.path.abspath('')
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


# execute main function
if __name__ == '__main__':
    main()
