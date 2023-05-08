# Import necessary libraries
from googletrans import Translator
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Define function to translate and speak French text
def translate_and_speak_french(text):
    # Create a translator object
    translator = Translator()

    # Use the translator to translate the text to French
    translated_text = translator.translate(text, dest='fr').text

    # Print the translated text
    print(f"Translated text (French): {translated_text}")

    # Set the voice to use a French accent
    voice_id = "com.apple.speech.synthesis.voice.thomas"

    # Use pyttsx3 to speak the translated text with the French accent
    engine.setProperty('voice', voice_id)
    engine.say(translated_text)
    engine.runAndWait()


# Define function to translate and speak Italian text
def translate_and_speak_italian(text):
    # Create a translator object
    translator = Translator()

    # Use the translator to translate the text to Italian
    translated_text = translator.translate(text, dest='it').text

    # Print the translated text
    print(f"Translated text (Italian): {translated_text}")

    # Set the voice to use an Italian accent
    voice_id = "com.apple.speech.synthesis.voice.alice"

    # Use pyttsx3 to speak the translated text with the Italian accent
    engine.setProperty('voice', voice_id)
    engine.say(translated_text)
    engine.runAndWait()


# Define function to translate and speak Chinese text
def translate_and_speak_chinese(text):
    # Create a translator object
    translator = Translator()

    # Use the translator to translate the text to Chinese
    translated_text = translator.translate(text, dest='zh-CN').text

    # Print the translated text
    print(f"Translated text (Chinese): {translated_text}")

    # Set the voice to use a Chinese accent
    voice_id = "com.apple.speech.synthesis.voice.ting-ting"

    # Use pyttsx3 to speak the translated text with the Chinese accent
    engine.setProperty('voice', voice_id)
    engine.say(translated_text)
    engine.runAndWait()


# Prompt user to enter the text to be translated
text = input("Enter text to be translated: ").strip()

# Prompt user to enter the language to translate to
language = input(
    "Enter language to translate to (French, Italian, or Chinese): ").strip()

# Call the appropriate translation function based on the chosen language
if language.lower() == "french":
    translate_and_speak_french(text)
elif language.lower() == "italian":
    translate_and_speak_italian(text)
elif language.lower() == "chinese":
    translate_and_speak_chinese(text)
else:
    print("Invalid language specified")
