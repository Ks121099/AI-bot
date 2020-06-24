import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import pyautogui
# import wikipedia
import pyjokes
import vlc
import os
import psutil

engine = pyttsx3.init()

rate = engine.getProperty('rate')   

month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is " + Time)

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage )
    battery=psutil.sensors_battery()
    speak("Current battery is at "+str(battery.percent)+"percent")

def date():
    y = str(datetime.datetime.now().year)
    m = datetime.datetime.now().month
    d = str(datetime.datetime.now().day)
    speak("Today's Date is " + d+" "+month[m-1]+" "+y)

# def song():
#     p=vlc.MediaPlayer(r"C:\Users\Admin\Desktop\webd\projects\Jarvis\COCACOLA.mp3")
#     p.play()

def joke():
    speak(pyjokes.get_joke())

def greeting():
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
    speak(greet+" , ,Jarvis at your service, Please tell me how can I help you?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1  # wait time
        audio = r.listen(source=source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query

def ss():
    pic=pyautogui.screenshot()
    pic.save(r"C:\Users\Admin\Desktop\webd\projects\Jarvis\\screenshot.png")

if __name__ == "__main__":
    greeting()
    while True:
        ip = command().lower()
        if 'time' in ip:
            time()
        elif 'date' in ip:
            date()
        elif 'chrome' in ip:
            speak("Sure sir, But which website should I open in google chrome")
            path1= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            ip1= command().lower()
            wb.get(path1).open_new_tab(ip1+'.com')

           
        elif 'screenshot' in ip:
            ss()
            speak("Its Done!! The screenshot has been saved in the respective folder")
        elif 'cpu' in ip:
            cpu()
        elif 'joke' in ip:
            engine.setProperty('rate', 175)  
            joke()
            engine.setProperty('rate', 200)  
        elif 'logout'in ip:
            os.system("shutdown -l")
        elif 'shutdown'in ip:
            os.system("shutdown /s /t 1")
        elif 'restart'in ip:
            os.system("shutdown /r /t 1")
        elif 'offline' in ip:
            speak("Ok sir, as you say , I am Going offline")
            quit()

        speak("What else can I do for you sir?")
