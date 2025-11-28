import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand.")
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("❌ Network error.")
        speak("Network problem. Try again.")
        return ""

def save_note(note):
    """Save note to a timestamped text file."""
    os.makedirs("notes", exist_ok=True)
    filename = f"notes/note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(note)
    print(f"✅ Saved note to {filename}")
    speak("Note saved.")

# MAIN LOOP
speak("Speech notepad is ready. Speak your note or say 'stop' to exit.")

while True:
    text = listen()
    if text.lower() in ["stop", "exit", "quit"]:
        speak("Goodbye!")
        break
    elif text:
        save_note(text)

speak("Goodbye!")