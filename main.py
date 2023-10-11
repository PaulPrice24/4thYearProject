import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import os
import time

#Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 = male, 1 = female
activationWord = 'computer'

# Configure browser
# Set the path
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate =120): #rate is speed of AI voice
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('Sorry, I did not catch that')
        speak('Sorry, I did not catch that')
        print(exception)
        return 'None'
    
    return query

# main loop
if __name__ == '__main__':
    speak('Welcome, how may I help you today?')

    while True:
        # parse as list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Hello, nice to meet you')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

            # Navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)

            if query[0] == 'play' and query[1] == 'music':
                listener = sr.Recognizer()
                speak('What would you like to play?')

                with sr.Microphone() as source:
                    listener.pause_threshold = 2
                    input_speech = listener.listen(source)

                try:
                    print('Recognizing speech...')
                    song = listener.recognize_google(input_speech, language='en_gb')
                    print(f'The input speech was: {song}')
                    os.system("spotify")
                    time.sleep(10)
                    pyautogui.hotkey('ctrl', 'l')
                    time.sleep(2)
                    pyautogui.write(song, interval = 0.1)

                    for key in ['enter', 'tab', 'enter', 'tab', 'enter']:
                        time.sleep(2)
                        pyautogui.press(key)

                except Exception as exception:
                    print('Sorry, I did not catch that')
                    speak('Sorry, I did not catch that')
                    print(exception)

            if query[0] == 'search':
                speak('Searching...')
                query = ' '.join(query[1:])
                webbrowser.open('https://www.google.com/search?q=' + query)

            if query[0] == 'what' and query[1] == 'time' and query[2] == 'is' and query[3] == 'it':
                speech = datetime.datetime.now().strftime("%H:%M")
                speak(speech)

            if query[0] == 'exit':
                speak('Goodbye')
                break