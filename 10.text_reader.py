import pyttsx3
import pyperclip
import time

# Define a function to speak the given text
def speak_text(text):
    engine = pyttsx3.init()
    # Set British English voice (female)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.moira')
    engine.say(text)
    engine.runAndWait()

# Get the initial clipboard contents
prev_text = pyperclip.paste()

# Start the main loop
while True:
    # Check if the clipboard contents have changed
    current_text = pyperclip.paste()
    if current_text != prev_text:
        speak_text(current_text)
        prev_text = current_text

    # Wait for a short interval before checking again
    time.sleep(0.1)
