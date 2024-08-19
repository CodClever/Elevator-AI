import base64
import sys

import pyttsx3  # pip install pyttsx3
import os  # pip install os
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbrowser
import openai  # pip install openai
from django.contrib.sites import requests
from google import generativeai
import google.generativeai as genai # pip install google-generativeai
from config import apikey
import datetime  # pip install datetime
import random  # pip install random
import numpy as np  # pip install numpy

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)

chatStr = ""


# Source: https://youtu.be/Z3ZAJoi4x6Q


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"{Username}: {query}\n Elevator AI: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        chat(query)


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        # print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        ai(prompt)


# Speaking function    :-


def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        speak(audio)


# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    try:
        global chatStr
        print(chatStr)
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        chat(query)


def ai(prompt):
    try:
        text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(
                f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w"
        ) as f:
            f.write(text)
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        ai(prompt)


def say(text):
    try:
        os.system(f'say "{text}"')
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        say(text)


def takeCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # r.pause_threshold =  0.6
            audio = r.listen(source)
            try:
                print("Recognizing...")
                speak("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query
            except Exception:
                return "Some Error Occurred. Sorry from Elevator A.I"
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        takeCommand()


def _on_update_interval():
    try:
        pass
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        _on_update_interval()


_on_update_interval()

print("Elevator AI")
speak("Elevator AI")
print(
    "Hello, My name is Arinjay Kumar. I am the founder of this AI. I hope you like it."
)
print("Enjoy!")
Username = str(input("Please enter your username to continue: "))


def the_main():
    try:
        if Username == "Arinjay":
            print("Your name is same as our founder i.e. Arinjay Kumar")
        elif Username == "":
            print("Please write your preferred username:")
            speak("Please write your preferred username:")
        elif Username == "arinjay":
            print("Your name is same as our founder i.e. Arinjay Kumar")
        elif Username == "Arinjay Kumar":
            print("Your name is same as our founder i.e. Arinjay Kumar")
        elif Username == "arinjay kumar":
            print("Your name is same as our founder i.e. Arinjay Kumar")
        elif Username == "Arinjay kumar":
            print("Your name is same as our founder i.e. Arinjay Kumar")            
        elif Username == "arinjay Kumar":
            print("Your name is same as our founder i.e. Arinjay Kumar")            
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        the_main()


the_main()

Usernameage = int(input("Please enter your current age for verification: "))


def the_main_v():
    try:
        if Usernameage >= 18:
            print("🔃 Loading 🔃")        
        if Usernameage <= 120:
            print("🔃 Loading 🔃")            
        if Usernameage <= 18:
            print("You are not allowed!")            
            int(input("Please enter your current age for verification: "))
        if Usernameage >= 120:
            print("You are not allowed!")            
            int(input("Please enter your current age for verification: "))
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        the_main_v()


the_main_v()

print("Hello,", Username)
print("🔃 Loading 🔃")
print("Fixing screws")
print("Starting engine")
print("Ready!")
print("** Warning **")
print(
    "This is in beta stage and is currently in development. We strictly do not recommend users to give any personal "
    "information on this app."
)
print("🔃 Loading 🔃")

q1 = "Who is me?"
q11 = "who is me"
q111 = "Who is me"
q1111 = "who is me?"

q2 = "Who is your founder?"
q22 = "who is your founder"
q222 = "Who is your founder"
q2222 = "who is your?"

q3 = "Who are you?"
q33 = "who are you"
q333 = "Who are you"
q3333 = "who are you?"

List=[
    "1. OpenAI's ChatGPT 3.5",
    "2. Google's Gemini 1.0 AI",
    "3. Stability XL 1024 1.0",
    "4. Or continue with Elevator AI..."
]
print(List)

Diversion = str(input("Please enter the number of the AI model you are going to use: "))


def chat_List_Def():
    if Diversion == "1. OpenAI's ChatGPT 3.5" or 1:
        chatgpt()
    elif Diversion == "2. Google's Gemini 1.0 AI" or 2:
        gemini()
    elif Diversion == "3. Stability XL 1024 1.0" or 3:
        stability()
    elif Diversion == "4. Or continue with Elevator AI..." or 4:
        the_maingame()
    else:
        print("Elevator AI -> That is not what I expected!")
        print("Elevator AI -> Please try again by restarting the application.")
        sys.exit()


chat_List_Def()


def chatgpt():
    def chat():

        input = input("Please enter your ChatGPT API Key from https://platform.openai.com/api-keys -> ")

        openai.api_key = input

        maininput = input("You -> ")

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=maininput,
            temperature=0.2,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print("ChatGPT -> ", response)

        def loop():
            if chat():
                chat()
                loop()
            else:
                chat()
                loop()

        loop()


def gemini():
    def chat():
        maininput = input("Please enter your Gemini API Key from https://aistudio.google.com/app/prompts/new_chat -> ")
        input = input("You -> ")

        print("""

        I am still under development, and there are many things that I do not know. If I don't know the answer to a question, I will say so honestly. I will also try to provide some context or resources that may help you find the answer yourself. For example, I might say something like "I'm not sure about that, but I can find out for you. Can you give me more information about what you're looking for?" or "I'm not familiar with that topic, but I can provide you with some links to relevant websites."

        I am always learning new things, and I am committed to providing accurate and helpful information to my users. If you ever notice that I have made a mistake, please feel free to let me know. I appreciate your feedback and will use it to improve my performance.

        """)

        """
        At the command line, only need to run once to install the package via pip:

        $ pip install google-generativeai
        """

        genai.configure(api_key="maininput")

        # Set up the model
        generation_config = {
            "temperature": 1,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        convo = model.start_chat(history=[
        ])

        convo.send_message("input")
        print(convo.last.text)

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()

    loop()


def stability():
    def chat():
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

        maininput = input("Please enter your Stability API Key from https://platform.stability.ai/account/keys -> ")

        input = input("Your prompt -> ")
        input2 = input("How you want it to look like? Separate your options by a comma -> ")

        text_Prompt = input
        prompt_type = input2

        body = {
            "steps": 40,
            "width": 1024,
            "height": 1024,
            "seed": 0,
            "cfg_scale": 5,
            "samples": 1,
            "text_prompts": [
                {
                    "text": text_Prompt,
                    "weight": 1
                },
                {
                    "text": prompt_type,
                    "weight": -1
                }
            ],
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": maininput,
        }

        response = requests.post(
            url,
            headers=headers,
            json=body,
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        # make sure the out directory exists
        if not os.path.exists("./output"):
            os.makedirs("./output")

        for i, image in enumerate(data["artifacts"]):
            with open(f'./output/tti_{image["seed"]}.png', "wb") as f:
                f.write(base64.b64decode(image["base64"]))

        print("Elevator AI -> Finished, check this directory.")

    def loop():
        if chat():
            chat()
            loop()
        else:
            chat()
            loop()

    loop()


Chat = str(input("Please write what you like to say: "))


def the_maingame():
    query = Chat

    try:
        if "Wikipedia" in query:
            print("Finding...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia : ")
            speak("According to Wikipedia : ")
            print(results)
            speak(results)
        if "What" in query:
            print("Finding...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia : ")
            speak("According to Wikipedia : ")
            print(results)
            speak(results)
        if "what" in query:
            print("Finding...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia : ")
            speak("According to Wikipedia : ")
            print(results)
            speak(results)
        if "Who" in query:
            print("Finding...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia : ")
            speak("According to Wikipedia : ")
            print(results)
            speak(results)
        if "who" in query:
            print("Finding...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia : ")
            speak("According to Wikipedia : ")
            print(results)
            speak(results)
        if query == q1:
            print("You are ", Username)
            str(input("Please write what you like to say: "))
        if query == q11:
            print("You are ", Username)
            str(input("Please write what you like to say: "))
        if query == q111:
            print("You are ", Username)
            str(input("Please write what you like to say: "))
        if query == q1111:
            print("You are ", Username)
            str(input("Please write what you like to say: "))

        if query == q2:
            print("I am founded by the ElevatorAI Developer Team.")
            speak("I am founded by the ElevatorAI Developer Team.")
            str(input("Please write what you like to say: "))
        if query == q22:
            print("I am founded by the ElevatorAI Developer Team.")
            speak("I am founded by the ElevatorAI Developer Team.")
            str(input("Please write what you like to say: "))
        if query == q222:
            print("I am founded by the ElevatorAI Developer Team.")
            speak("I am founded by the ElevatorAI Developer Team.")
            str(input("Please write what you like to say: "))
        if query == q2222:
            print("I am founded by the ElevatorAI Developer Team.")
            speak("I am founded by the ElevatorAI Developer Team.")
            str(input("Please write what you like to say: "))

        if query == q3:
            print(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            speak(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            str(input("Please write what you like to say: "))
        if query == q33:
            print(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            speak(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            str(input("Please write what you like to say: "))
        if query == q333:
            print(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            speak(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            str(input("Please write what you like to say: "))
        if query == q3333:
            print(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            speak(
                "I am an AI(Artificial Intelligence) made by my founder - Mr. Arinjay Kumar."
            )
            str(input("Please write what you like to say: "))

        else:
            print("Sorry, I have not gained that particular information yet.")
            speak("Sorry, I have not gained that particular information yet.")
            print("You can make me learn it, please write the answer then : ")
            speak("You can make me learn it, please write the answer then : ")
            userinput = input(
                "You can make me learn it, please write the answer then : "
            )
    except Exception:
        print("Some problem occurred!")
        speak("Some problem occurred!")
        the_maingame()

        def userinput_change():
            try:
                if userinput != query:
                    name = open("usernames.txt", "w")
                    name.write(userinput)
                    name.close()

                    open1 = open("usernames.txt", "r")
                    print(open1.read())
            except Exception:
                print("Some problem occurred!")
                speak("Some problem occurred!")
                userinput_change()

        str(input("Please write what you like to say: "))


the_maingame()

print("The End!")
speak("The End!")


def on_update_interval():
    pass
