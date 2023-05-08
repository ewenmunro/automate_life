# libraries
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from dotenv import load_dotenv
import speech_recognition as sr
from bs4 import BeautifulSoup
from fpdf import FPDF
import pyttsx3
import datetime
import webbrowser
import requests
import subprocess
import pyperclip
import random
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
    
    
# hiking randomizer
def hiking_randomizer():
    locations = []

    selected_location = random.choice(locations)
    speak(f"Go to: {selected_location}")
    
    
# cinema times
def get_cinema_times():
    # insert url
    url = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('ul', {'class': 'Sessions'})
    cinema_times = []
    for movie in movies:
        title = movie.find('li', {'data-name': True}).get('data-name').strip()
        times = [time.text for time in movie.find_all(
            'span', {'class': 'Time'})]
        cinema_times.append({'title': title, 'times': times})

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f"Tomorrow's Cinema Times:", 0, 1)
    pdf.set_font('Arial', '', 12)
    for movie in cinema_times:
        pdf.cell(0, 10, movie['title'], 0, 1)
        for time in movie['times']:
            pdf.cell(10)
            pdf.cell(0, 10, time, 0, 1)
        pdf.cell(0, 10, '', 0, 1)

    pdf.output('cinema_times.pdf')
    speak(f"Printing tomorrow's cinema times")
    
    
# convert currencies
def get_currency():
    currency_rates = CurrencyRates()

    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say the currency code to convert from:")
                audio = r.listen(source)
            from_currency = r.recognize_google(audio)

            with sr.Microphone() as source:
                speak("Say the currency code to convert to:")
                audio = r.listen(source)
            to_currency = r.recognize_google(audio)

            with sr.Microphone() as source:
                speak("Say the amount to be converted:")
                audio = r.listen(source)
            amount = float(r.recognize_google(audio))

            result = currency_rates.convert(from_currency, to_currency, amount)
            speak("{0} {1} is equal to {2} {3}".format(
                amount, from_currency, result, to_currency))
            break

        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Please try again.")
        except sr.RequestError:
            speak(
                "Sorry, I'm having trouble accessing the speech recognition service. Please try again later.")
            break
        except RatesNotAvailableError:
            speak(
                "Sorry, the currency rates are not available at the moment. Please try again later.")
            break


# open any app on computer
def open_app(app_name):
    subprocess.call(["open", "-a", app_name])
    speak("Opening " + app_name)
    
    
# open vs code
def open_vs_code():
    subprocess.call(["open", "-a", "Visual Studio Code"])
    speak("Opening VS Code")


# open terminal
def open_terminal():
    subprocess.call(["open", "-a", "Terminal"])
    speak("Opening Terminal")


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
        
        
# decision maker
def decision_maker():
    speak("How many options are you choosing from?")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
        num_options = int(r.recognize_google(audio))
        options = []
        for i in range(num_options):
            speak(f"What's option number {i+1}?")
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                option = r.recognize_google(audio)
                speak(f"You said {option}.")
                options.append(option)
            except:
                speak("I'm sorry, I didn't catch that.")
                options.append("")
                continue
            if i != num_options - 1:
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    if r.recognize_google(audio).lower() == "stop":
                        break
                except:
                    pass
        if options:
            random_option = random.choice(options)
            speak("I suggest you choose " + random_option)
    except:
        speak("I'm sorry, I didn't catch that.")


# password generator
def generate_spoken_password(length):
    digits = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
    password = ""
    for i in range(length):
        password += random.choice(digits[1:]) + " "
    return password.strip()


def password_generator():
    length = 4
    spoken_password = generate_spoken_password(length)
    speak(f"Your generated password is {spoken_password}")
    
    
# respond to saying thank you
def respond_to_thank_you():
    speak("You're welcome!")


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
            
        elif "hike" in text or "hiking" in text or "hiking randomizer" in text or "walk" in text or "walking" in text or "walking randomizer" in text:
            hiking_randomizer()

        elif "cinema times" in text:
            get_cinema_times()

        elif "currency" in text:
            get_currency()

        elif "app" in text:
            if "open " in text:
                app_name = text.split("open ")[1]
                open_app(app_name)
            else:
                speak("Sorry, I didn't catch the app name.")

        elif "mail" in text or "email" in text:
            open_mail()
            
        elif "vs code" in text or "code" in text:
            open_vs_code()

        elif "terminal" in text:
            open_terminal()

        elif "website" in text:
            open_website()

        elif "read text" in text or "read txt" in text:
            read_highlighted_text()

        elif "file manager" in text or "move file" in text or "move files" in text:
            file_manager("/to/file_path/1",
                         "/to/file_path/2", "pdf")
            
        elif "decide for me" in text:
            decision_maker()

        elif "password" in text:
            password_generator()

        elif "thank you" in text or "thanks" in text or "cheers" in text:
            respond_to_thank_you()

        elif "exit" in text or "axit" in text or "go to sleep" in text or "sleep" in text:
            speak("Goodbye!")
            break


# execute main function
if __name__ == '__main__':
    main()
