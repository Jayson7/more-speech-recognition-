import speech_recognition as sr
import webbrowser
from datetime import datetime
import pyttsx3

# Text-to-speech engine
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
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand.")
        speak("Sorry, I didn't catch that.")
        return ""

    except sr.RequestError:
        print("❌ API Error.")
        speak("Network problem. Try again.")
        return ""


def handle_command(command):
    """Handle voice commands."""
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        response = f"The time is {current_time}"
        print(response)
        speak(response)

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube now.")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I don't know that command yet.")
    
    return True


# MAIN LOOP
speak("Voice assistant ready. Say a command.")
running = True

while running:
    user_command = listen()
    if user_command:
        running = handle_command(user_command)

speak("Goodbye!")