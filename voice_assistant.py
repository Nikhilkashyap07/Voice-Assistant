import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import time
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, Not Understand")

# sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    # print(rate)
    engine.say(x)

    engine.runAndWait()

# speechtx("hello  Nikhil i am your voice assistant")    

if __name__ == '__main__':

    if "hey alexa" in sptext().lower():

        while True:
            data1 = sptext().lower()

            if "what is your name" in data1:
                name = "My name is Nikhil"
                speechtx(name)

            elif "old are you" in data1:
                age = "I am 20 years old"
                speechtx(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
                
            elif 'youtube' in data1:
                webbrowser,open('https://www.youtube.com/watch?v=Vh0xw9t88SA&t=2275s')    

            elif "joke" in data1:
                joke_1=pyjokes.get_joke(language="hu",category="chuck")
                print(joke_1)
                speechtx(joke_1)

            # elif "play song" in data1:
            #     address = "C:\Users\lenovo\OneDrive\Desktop\Sourabh\Ringtones"    
            #     listsong = os.listdir(address)
            #     print(listsong)
            #     os.startfile(os.path.join(address.listsong[0]))
            
            elif "exit" in data1:
                speechtx("thank you")
                break
            time.sleep(3)

else:
    print("Thanks")



    

    
