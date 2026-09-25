import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text,language='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    voices = engine.getProperty('voices')

    if language == 'en':
        engine.setProperty('voice', voices[0])  # Default voice for English
    elif language == 'es':
        engine.setProperty('voice', voices[1]) 

    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak in english")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio.")
    except sr.RequestError as e:
        print(f"api not working; {e}")
    return""  
def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text
def display_language_options():
    print("Select a language for translation:")
    print("1. hindi (hi)")
    print("2. tamil (ta)")
    print("3. telugu (te)")
    print("4. bengali (bn)")
    print("5. marathi (mr)")
    print("6. gujarati (gu)")
    print("7. punjabi (pa)")
    print("8. malayalam (ml)")

    choice = input("Enter the number corresponding to your choice:(1-8) ")
    language_dict = {
        '1': 'hi',
        '2': 'ta',
        '3': 'te',
        '4': 'bn',
        '5': 'mr',
        '6': 'gu',
        '7': 'pa',
        '8': 'ml'
    }
    return language_dict.get(choice, 'es')
def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language)
        speak(translated_text, language="en")
        print("translation spoken out")
if __name__ == "__main__":
    main()
