import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "open messenger" in c:
        webbrowser.open("https://www.messenger.com")
        speak("Opening Messenger")
    elif "open ai" in c:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")
    elif "open github" in c:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")
    elif "open twitter" in c:
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter")
    elif "open reddit" in c:
        webbrowser.open("https://www.reddit.com")
        speak("Opening Reddit")
    elif "open stack overflow" in c:
        webbrowser.open("https://www.stackoverflow.com")
        speak("Opening Stack Overflow")
    elif "open wikipedia" in c:
        webbrowser.open("https://www.wikipedia.org")
        speak("Opening Wikipedia")
    elif "play music" in c:
        webbrowser.open("https://www.spotify.com")
        speak("Opening Spotify")
    elif "open spotify" in c:
        webbrowser.open("https://www.spotify.com")
        speak("Opening Spotify")
    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please say the song name after 'play'.")
    elif "exit" in c or "quit" in c:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Yes , I am listening...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "hello" in word.lower():
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out. Waiting again...")
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
        except Exception as e:
            print("Error:", e)
