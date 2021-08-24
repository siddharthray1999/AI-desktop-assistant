import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[0].id)
engine.setProperty('Voice',voice[0].id)





# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout = 10 ,phrase_time_limit= 15)

    try:
        print("recognizing......")
        query = r.recognize_google(audio ,language= 'en - in')
        print(f"user said : {query}")

    except Exception as e:
        speak("say that again please")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <=12:
        speak("Good Morning Sir")
        speak("I am jarvis.please tell me how can i assist you")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir")
        speak("I am jarvis.please tell me how can i assist you")
    else:
        speak("Good evening Sir")
        speak("I am jarvis.please tell me how can i assist you")

# send email
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('siddharthray47@gmail.com','Rinku8130186780')
    server.sendmail('siddharthray47@gmail.com',to ,content)
    server.close()


if  __name__=='__main__':
    wish()
    while True:
        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt"  in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "F:\\New folder (2)"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")


        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif"open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open Google" in query:
            speak("sir,what should i search in google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif"play songs on youtube" in query:
            kit.playonyt("see you again")

        elif" email to pinky" in query:
            try:
                speak("what should i say ?")
                content = takecommand().lower()
                to = "raypinky053@gmail.com"
                sendEmail = "content"
                speak("email has been send to pinky ray")

            except Exception as e:
                print(e)

        elif "no thaks" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()


            speak("sir, do you have any other work")
