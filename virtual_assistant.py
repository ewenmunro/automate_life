# libraries
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import subprocess
import pyperclip
import shutil
import os


# for api keys
load_dotenv()


# voice recognition
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now:")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except:
            print("Sorry, could not recognize your voice.")
            return ""


# speaker
def speak(text):
    engine = pyttsx3.init()
    voice_id = "com.apple.speech.synthesis.voice.moira"
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()


# get date and time
def get_date_time():
    now = datetime.datetime.now()
    date = now.strftime("%A, %B %d, %Y")
    time = now.strftime("%I:%M %p")
    return date, time


# search the web
def search_web():
    speak("What would you like me to search for?")
    text = get_audio()
    if text:
        url = "https://search.brave.com/search?q=" + text
        webbrowser.get().open(url)
        speak("Here is what I found for " + text)


# get the weather for anywhere
def get_weather():
    city_name = speak(
        "What is the name of the city you want to know the weather for?")
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city_name}"
    text = get_audio()
    if text:
        city = text.lower()
        r = requests.get(url.format(city)).json()
        if "current" in r:
            weather = r["current"]["weather_descriptions"][0]
            temperature = r["current"]["temperature"]
            humidity = r["current"]["humidity"]
            wind_speed = r["current"]["wind_speed"]
            speak(f"The weather in {city.title()} is {weather}. The temperature is {temperature} degrees Celsius. The humidity is {humidity} percent. The wind speed is {wind_speed} meters per second.")
        else:
            speak("Sorry, I could not find the weather details for the given city.")


# get directions using google maps
def get_directions():
    speak("What is the starting point?")
    start = get_audio()
    speak("What is the destination?")
    destination = get_audio()
    speak("What mode of transportation do you want to use? (driving, walking, bicycling, transit)")
    mode = get_audio().lower()
    while mode not in ["driving", "walking", "bicycling", "transit"]:
        speak("Invalid mode of transportation. Please choose from driving, walking, bicycling, or transit.")
        mode = get_audio().lower()
    url = f"https://www.google.com/maps/dir/{start}/{destination}/@{mode}"
    webbrowser.get(
        using='open -a /Applications/Brave\ Browser.app %s').open(url)
    speak(f"Here are the {mode} directions from {start} to {destination}")


# open any app on computer
def open_app(app_name):
    subprocess.call(["open", "-a", app_name])
    speak("Opening " + app_name)


# open mail
def open_mail():
    subprocess.call(["open", "-a", "Mail"])
    speak("Opening Mail")


# open any website
def open_website():
    speak("What website would you like me to open?")
    text = get_audio()
    if text:
        url = "https://" + text
        webbrowser.get(
            using='open -a /Applications/Brave\ Browser.app %s').open(url)
        speak("Opening " + text)


# read highlighted text
def read_highlighted_text():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    text = pyperclip.paste()
    engine.say(text)
    engine.runAndWait()


# file manager
def file_manager(source_dir, dest_dir, filenames):
    for filename in filenames:
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(dest_dir, filename)
        shutil.move(src_path, dst_path)
        speak("Organising files")


# main function
def main():
    speak("Hi, how can I help you?")

    while True:
        text = get_audio().lower()

        if "date" in text:
            date, time = get_date_time()
            speak("Today is " + date + " and the time is " + time)

        elif "search" in text:
            search_web()

        elif "weather" in text:
            get_weather()

        elif "directions" in text or "map" in text or "maps" in text:
            get_directions()

        elif "app" in text:
            if "open " in text:
                app_name = text.split("open ")[1]
                open_app(app_name)
            else:
                speak("Sorry, I didn't catch the app name.")

        elif "mail" in text or "email" in text:
            open_mail()

        elif "website" in text:
            open_website()

        elif "read text" in text or "read txt" in text:
            read_highlighted_text()

        elif "file manager" in text or "move file" in text or "move files" in text:
            file_manager("/to/file_path/1",
                         "/to/file_path/2", "pdf")

        elif "exit" in text or "axit" in text or "go to sleep" in text or "sleep" in text:
            speak("Goodbye!")
            break


# execute main function
if __name__ == '__main__':
    main()
