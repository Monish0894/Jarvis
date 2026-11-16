import requests
import speech_recognition as sr
import os
import pyttsx3
from llama_cpp import Llama

# Initialize the pyttsx3 engine globally
engine = pyttsx3.init()


# Load the LLaMA model (Ensure you have the correct GGUF model path)
llm = Llama(model_path="D:\moni\Llama-3.2-1B-Instruct-IQ3_M.gguf", n_ctx=512) # Replace your model path

# Function to convert speech to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=15)
            print("Processing your speech...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice. Please try again.")
            return None
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start. Please speak louder.")
            return None

# Function to get AI response using llama-cpp-python
def get_ai_response(prompt):
    url = "http://localhost:8080/completion"  # Change if running on another machine
    data = {"prompt": prompt, "max_tokens": 150}
    
    try:
        response = requests.post(url, json=data)
        response_json = response.json()
        message = response_json["choices"][0]["text"].strip()
        print(f"AI: {message}")
        return message
    except Exception as e:
        print("Error accessing Llamafile server:", e)
        return "Sorry, I encountered an error."
# Function to convert text to speech
def speak_text(text):
    try:
        # Get the available voices
        voices = engine.getProperty('voices')

        # Set the male voice by index (e.g., voices[0])
        engine.setProperty('voice', voices[0].id)  # Replace 0 with the index of the male voice

        # Set the speech rate (default is around 200)
        engine.setProperty('rate', 150)  # Adjust for slower or faster speech

        # Speak the provided text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error with Text-to-Speech:", e)

# Main function to run the AI assistant
def jarvis():
    print("Hello! I am Jarvis, your AI assistant.")
    speak_text("Hello! I am Jarvis, your AI assistant.")
    while True:
        print("\nSay 'exit' to stop the assistant.")
        query = recognize_speech()
        if query is None:
            continue
        if "exit" in query.lower():
            print("Goodbye!")
            speak_text("Goodbye!")
            break

        # Custom Commands
        if "open YouTube" in query.lower():
            print("Opening YouTube...")
            speak_text("Opening YouTube.")
            os.system("start https://www.youtube.com")
            continue

        elif "play music" in query.lower():
            print("Playing music...")
            speak_text("Playing music.")
            os.system("start https://www.spotify.com")  # Or play a local MP3 file
            continue

        elif "what is the time" in query.lower():
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"The current time is {current_time}")
            speak_text(f"The current time is {current_time}.")
            continue

        elif "open Google" in query.lower():
            print("Opening Google...")
            speak_text("Opening Google.")
            os.system("start https://www.google.com")
            continue

        elif "open notepad" in query.lower():
            print("Opening Notepad...")
            speak_text("Opening Notepad.")
            os.system("notepad")
            continue

        elif "open calculator" in query.lower():
            print("Opening Calculator...")
            speak_text("Opening Calculator.")
            os.system("calc")
            continue

        elif "tell me a joke" in query.lower():
            joke = "Why don't scientists trust atoms? Because they make up everything!"
            print(joke)
            speak_text(joke)
            continue

        elif "calculate" in query.lower():
            try:
                expression = query.lower().replace("calculate", "").strip()
                result = eval(expression)  # Use eval cautiously; sanitize input in production
                print(f"The result is {result}")
                speak_text(f"The result is {result}.")
            except:
                print("I couldn't calculate that. Please try again.")
                speak_text("I couldn't calculate that. Please try again.")
            continue

        elif "search for" in query.lower():
            search_term = query.lower().replace("search for", "").strip()
            print(f"Searching Google for {search_term}...")
            speak_text(f"Searching Google for {search_term}.")
            os.system(f"start https://www.google.com/search?q={search_term}")
            continue

        # Get AI-generated response
        response = get_ai_response(query)
        # Speak the response
        speak_text(response)

# Run the assistant
if __name__ == "__main__":
    jarvis()
