import speech_recognition as sr, pyttsx3, webbrowser 
from datetime import datetime
#initialise 
recogniser = sr.Recognizer() 
engine = pyttsx3.init() 

#speak function 
def speak(text):
    print('Assistant: ', text) 
    engine.say(text) 
    engine.runAndWait() 

#listen function 
def listen():
    with sr.Microphone() as mic:
        audio = recogniser.listen(mic)
        try:
            text = recogniser.recognize_google(audio)
            print('You: ', text)
            return text.lower()
        except sr.UnknownValueError:
            speak('Iam unable to understand, please speak again')
            return ''
        except sr.RequestError:
            speak('Iam unable to connect to the service')
            return ''

print('Hi welcome to voice assistant, how can i help you')
while True:
    command = listen() 
    #saying HI 
    if 'hello' in command:
        speak('Hi, how can i help you?') 
    elif 'time' in command: 
        curtime = datetime.now().strftime('%I:%M:%p') 
        speak('Current time is' + curtime)  
    elif 'open google' in command: 
        speak('Opening google')
        webbrowser.open('https://www.google.com') 
    elif 'open youtube' in command:
        speak('Opening youtube')
        webbrowser.open('https://www.youtube.com') 
    elif 'search' in command:
        command = command.replace('search', '', 1)
        speak('searching for' + command)
        webbrowser.open('https://www.google.com/search?q=' + command) 
    elif 'exit' in command:
        break
