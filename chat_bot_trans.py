import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    voices = engine.getProperty('voices')

    if language == 'en':
        engine.setProperty('voice', voices[0].id)  # English voice
    else:
        engine.setProperty('voice', voices[1].id)  # other voice

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak now.")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio.")
    except sr.RequestError as e:
        print(f"API not working; {e}")
    return ""

def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def display_language_options():
    print("language avaailable for translation:")
    print("1. hindi (hi)")
    print("2. tamil (ta)")
    print("3. telugu (te)")
    print("4. bengali (bn)")
    print("5. marathi (mr)")
    print("6. gujarati (gu)")
    print("7. malayalam (ml)")
    print("8. punjabi (pa)")

    choice = input("please select the target language number (1-8): ")
    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }
    return language_dict.get(choice, "es")  # Default to Spanish if invalid choice

def main():
    target_language = display_language_options()

    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language)
        speak(translated_text, language="en")

        print("translated spoken out:")
if __name__ == "__main__":
    main()

    