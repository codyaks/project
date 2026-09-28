import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..... speak now")
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio)
            print(f"you said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("could not understand the audio.")
        except sr.RequestError as e:
            print(f"api not working; {e}")
    return ""
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "exit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'am not sure how to help you")
    return True
def main():
    speak("voice assistant activated, say something.")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__ == "__main__":
    main()
