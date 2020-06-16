import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is " + Time)


def date():
    y = str(datetime.datetime.now().year)
    m = datetime.datetime.now().month
    d = str(datetime.datetime.now().day)
    speak("Today's Date is " + d+" "+month[m-1]+" "+y)

# def command():
#     r=sr.Recognizer
#     with sr.Microphone as source:
#         print("Listening.........")

def main():
    speak("Welcome Back Sir!!")
    date()
    time()
    h = datetime.datetime.now().hour
    if h > 4 and h <= 12:
        greet = " Good Morning Sir"
    elif h > 12 and h <= 16:
        greet = " Good Afternoon Sir"
    elif h > 16 and h <= 21:
        greet = " Good Evening Sir" 
    elif h > 21 and h <= 24:
        greet = " Good Night Sir"
    else:
        greet = " Good Night Sir"

    speak(greet+"Jarvis at your service, Please tell me how can I help you?")


main()
