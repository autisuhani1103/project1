import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pyjokes
import subprocess
import ctypes
import winshell
import time
import pywhatkit

print("You can call these commands-")
print("1. Wikipedia")
print("2. Open chrome")
print("3. Open google")
print("4. Open youtube")
print("5. Open stack overflow")
print("6. Open gmail")
print("7. Open playstore")
print("8. Open classroom")
print("9. Open meet")
print("10. Open drive")
print("11. Open calendar")
print("12. Microsoft edge")
print("13. Open visual studio code")
print("14. Open python")
print("15. Open microsoft store")
print("16. Open excel")
print("17. Open word")
print("18. Open desktop")
print("19. Open powerpoint")
print("20. Open anydesk")
print("21. Open C drive")
print("22. Open download")
print("23. Open map")
print("24. Lock window")
print("25. Play music")#hindi songs
print("26. Play songs")#marathi songs
print("27. Time")
print("28. Date")
print("29. Open calculator")
print("30. Open microsoft 365")
print("31. Shutdown system")
print("32. Restart system")
print("33. Hibernate")
print("34. Sleep")
print("35. Log off")
print("36. Signout")
print("37. Google search")
print("38. Play")  # Youtube songs
print("39. Empty recycle bin")
print("40. Joke")

time.sleep(3)
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Suhani. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hey I am Listening.....")
        speak('Hey I am Listening')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5)

    try:
        print("Recognizing....")
        data = r.recognize_google(audio)
        print("You said:", data)
        return data.lower()  # Convert the recognized text to lowercase
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

def execute_command(command):
    if 'wikipedia' in command:
        speak('opening Wikipedia...')
        codePath = ("https://www.wikipedia.org//")
        os.startfile(codePath)

    elif 'open chrome' in command:
        speak("opening chrome")
        codePath = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
        os.startfile(codePath)

    elif 'open youtube' in command:
        speak("opening youtube")
        wb.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("opening google")
        wb.open("https://www.google.co.in")

    elif 'open stackoverflow' in command:
        speak("opening stackoverflow")
        codePath = ("https://stackoverflow.com")
        os.startfile(codePath)

    elif 'open gmail' in command:
        speak("opening gmail")
        wb.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'open playstore' in command:
        speak("opening playstore")
        wb.open("https://play.google.com/store/games?hl=en_IN&gl=US")

    elif 'open classroom' in command:
        speak("opening classroom")
        wb.open("https://classroom.google.com")

    elif 'open meet' in command:
        speak("opening google meet")
        wb.open("https://meet.google.com/?hs=197&authuser=0")

    elif 'open drive' in command:
        speak("opening drive")
        wb.open("https://drive.google.com/drive/home")

    elif 'open calendar' in command:
        speak("opening calendar")
        wb.open("https://calendar.google.com/calendar/u/0/r")

    elif 'microsoft edge' in command:
        speak("opening microsoft edge")
        wb.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")

    elif 'open visual studio code' in command:
        speak("opening visual studio code")
        wb.open(
            "C:\\Users\\autis\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")

    elif 'open python' in command:
        speak("opening python")
        wb.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.11\\Python 3.11 (64-bit).lnk")

    elif 'open microsoft store' in command:
        speak("opening microsoft store")
        wb.open("https://apps.microsoft.com/home?hl=en-US&gl=US")

    elif 'open excel' in command:
        speak("opening excel")
        wb.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")

    elif 'open word' in command:
        speak("opening word")
        wb.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")

    elif 'open desktop' in command:
        speak("opening desktop")
        wb.open("C:\\Users\\autis\\Desktop")

    elif 'open powerpoint' in command:
        speak("opening powerpoint")
        wb.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

    elif 'open anydesk' in command:
        speak("opening anydesk")
        wb.open("C:\\Users\\autis\\Documents\\Downloads\\AnyDesk.exe")

    elif 'open c drive' in command:
        speak("opening C drive")
        wb.open("C:\\")

    elif 'open download' in command:
        speak("opening download")
        wb.open("C:\\Users\\Default\\Downloads")

    elif 'open map' in command:
        speak("opening map")
        wb.open("https://www.google.com/maps/@18.8181772,76.7698374,7z?authuser=0&entry=ttu")

    elif 'lock window' in command:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'play music' in command:
        speak("playing music")
        music_dir = "C:\\PROJECT\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'play songs' in command:
        speak("playing songs")
        music_dir = "C:\\PROJECT\\Songs"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M%p')
        speak('Current time ' + current_time)

    elif 'date' in command:
        current_date = datetime.datetime.today().strftime('%d / %m / %Y')
        speak("Today's date " + current_date)

    elif 'Open calculator' in command:
         speak("opening calculator")
         wb.open("https://www.calculator.net")

    elif 'Open microsoft 365' in command:
        speak("opening microsoft 365")
        wb.open("https://www.office.com")

    elif 'shutdown system' in command:
        speak("Hold on a sec! Your system is on its way to shutdown")
        subprocess.call(["shutdown", "/p", "/f"])

    elif 'restart system' in command:
        speak("Restarting")
        subprocess.call(["restart", "/r"])

    elif 'hibernate' in command:
        speak("Hibernating")
        subprocess.call(["hibernate", "/h"])

    elif 'sleep' in command:
        speak("Sleeping")
        subprocess.call(["sleep", "/s"])

    elif 'log off' in command:
        speak("Make sure all the applications are closed before logoff")
        time.sleep(5)
        subprocess.call(["logoff", "/l"])

    elif 'signout' in command:
        speak("Make sure all the applications are closed before signing off")
        time.sleep(5)
        subprocess.call(["signoff", "/S"])

    elif 'google search' in command:
        import wikipedia as googleScrap
        data = command.replace("google search", "")
        speak("This is what I found on the web!")
        pywhatkit.search(data)
        try:
            result = googleScrap.summary(data, 5)
            speak(result)
        except:
            speak("No special data available")

    elif 'play' in command:
        b = "playing youtube songs"
        wb.open("https://www.youtube.com//watch?v=4B8l493RrFQ")

    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif 'joke' in command:
        my_joke = pyjokes.get_joke(language="en", category="neutral")
        print(my_joke)
        speak(my_joke)


if __name__ == "__main__":
    wishMe()
    while True:
        user_command = input("Enter a command (type 'exit' to quit): ")
        if user_command.lower() == 'exit':
            break

        if user_command:
            execute_command(user_command)

        voice_command = takeCommand()
        if voice_command:
            execute_command(voice_command)
