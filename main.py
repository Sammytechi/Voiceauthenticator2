import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
     engine.say(text)
     engine.runAndWait()
def take_comand():
     try:
         with sr.Microphone() as source:
              print('listening...')
              voice = listener.listen(source)
              command = listener.recognize_google(voice)
              command = command.lower()
              if 'sammy' in command:
                  command = command.replace('sammy', '')
                  print(comand)
     except:
         pass
     return command

def run_sammy():
    command = take_comand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('curent time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif'date' in command:
        talk('sorry i am not interested')
    elif'are you single' in command:
        talk('yes i just got my own breakfast')
    elif'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please come again.')

while True:
    run_sammy()

run_sammy()
