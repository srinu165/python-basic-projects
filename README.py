import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Function to recognize voice commands"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return None

def send_email(to_email, subject, message):
    """Function to send an email"""
    try:
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, to_email, email_message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak("Failed to send email.")
        print(e)

def get_weather(city):
    """Function to fetch weather details"""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url).json()
    
    if "error" in response:
        speak("I couldn't fetch the weather information.")
    else:
        temp = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]
        speak(f"The weather in {city} is {condition} with a temperature of {temp}°C.")

def process_command(command):
    """Function to process the recognized command"""
    if command is None:
        return

    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What would you like me to search for?")
        query = recognize_speech()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")
    elif "wikipedia" in command:
        speak("What would you like to know from Wikipedia?")
        query = recognize_speech()
        if query:
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find anything on Wikipedia for that topic.")
    elif "email" in command:
        speak("Who do you want to send the email to?")
        recipient = recognize_speech()
        speak("What is the subject?")
        subject = recognize_speech()
        speak("What should the email say?")
        message = recognize_speech()
        if recipient and subject and message:
            send_email(recipient, subject, message)
    elif "weather" in command:
        speak("Which city's weather would you like to check?")
        city = recognize_speech()
        if city:
            get_weather(city)
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Advanced Voice Assistant activated. How can I help you?")
    while True:
        command = recognize_speech()
        process_command(command
