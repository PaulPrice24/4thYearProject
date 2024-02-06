import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import os
import wmi
import time
import openai
import pygetwindow as gw
import sounddevice as sd
import psutil
from phue import Bridge
from ip_address import bridge_ip_address
from dotenv import load_dotenv
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
load_dotenv()

#Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 = male, 1 = female
activationWord = 'computer'

# Configure browser
# Set the path
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

#light connection
b = Bridge(bridge_ip_address)
b.get_api()
b.get_light('Champs room')

def speak(text, rate =120): #rate is speed of AI voice
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def query_openai(prompt = ""):
    openai.organization = os.environ['OPENAI_ORG']
    openai.api_key = os.environ['OPENAI_API_KEY']

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,

    )

    return response.choices[0].text

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        print('Listening')
        speak('Listening')
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
                max_attempts = 3
                attempts = 0

                while attempts < max_attempts:

                    try:
                        speak('What would you like to play?')

                        with sr.Microphone() as source:
                            print('Listening')
                            speak('Listening')
                            listener.pause_threshold = 2
                            input_speech = listener.listen(source)

                        print('Recognizing speech...')
                        song = listener.recognize_google(input_speech, language='en_gb')
                        print(f'The input speech was: {song}')

                        os.system("spotify")
                        speak('Opening Spotify')
                        time.sleep(10)
                        pyautogui.hotkey('ctrl', 'l')
                        time.sleep(2)
                        pyautogui.write(song, interval=0.1)

                        for key in ['enter', 'tab', 'enter', 'tab', 'enter']:
                            time.sleep(2)

                            pyautogui.press(key)

                        spotify_window = gw.getWindowsWithTitle("Spotify")[0]
                        spotify_window.minimize()

                        break  # Exit the loop if successful
                    except sr.UnknownValueError:
                        attempts += 1
                        print('Sorry, I did not catch that')
                        speak('Sorry, I did not catch that')
                    except Exception as exception:
                        print(f'An error occurred: {exception}')
                        speak('An error occurred. Please try again.')

                if attempts == max_attempts:
                    print('Maximum attempts reached. Exiting.')
                    speak('Maximum attempts reached. Exiting.')

            if query[0] == 'question':
                query.pop(0)
                query = ' '.join(query)
                speech = query_openai(query)
                speak("Thinking")
                speak(speech)

            if query[0] == 'search':
                speak('Searching...')
                query = ' '.join(query[1:])
                webbrowser.open('https://www.google.com/search?q=' + query)

            if query[0] == 'what' and query[1] == 'time' and query[2] == 'is' and query[3] == 'it':
                speech = datetime.datetime.now().strftime("%H:%M")
                speak(speech)

            if query[0] == 'what' and query[1] == 'is' and query[2] == 'the' and query[3] == 'time':
                speech = datetime.datetime.now().strftime("%H:%M")
                speak(speech)

            if query[0] == 'turn' and query[1] == 'off':
                b.set_light('Champs room', 'on', False)

            if query[0] == 'turn' and query[1] == 'on':
                b.set_light('Champs room', 'on', True)

            if query[0] == 'increase':
                b.set_light('Champs room', 'bri', 254)

            if query[0] == 'dim':
                b.set_light('Champs room', 'bri', 80)

            if query[0] == 'exit':
                speak('Goodbye')
                break


            if query[0] == 'open':

                speak('Opening')
                
                pyautogui.hotkey('win', 's')
                appOpen = ' '.join(query[1:])
                time.sleep(2)
                pyautogui.write(appOpen, interval = 0.1)

                for key in ['enter']:
                    time.sleep(2)
                    pyautogui.press(key)

            if query[0] == 'terminate':

                speak('Closing')
                window_title = ' '.join(query[1:])

                # Close Word window
                word_window = gw.getWindowsWithTitle(window_title)
                if word_window:
                    word_window[0].close()
                    time.sleep(2)  # Add a delay to allow time for the window to close
                else:
                    print(f"Window with title '{window_title}' not found.")


            if query[0] == 'keyboard':
                query.pop(0)
                
                x = 1

                while x == 1:
                    listener = sr.Recognizer()
                    speak('Keyboard Control enabled')

                    with sr.Microphone() as source:
                        print('Listening')
                        speak('Listening')
                        listener.pause_threshold = 2
                        input_speech = listener.listen(source)

                    try:
                        print('Recognizing speech...')
                        appControl = listener.recognize_google(input_speech, language='en_gb')
                        print(f'The input speech was: {appControl}')

                        if appControl == 'search':
                            pyautogui.hotkey('ctrl', 'l')
                            
                        elif appControl == 'enable typing':
                            listener = sr.Recognizer()
                            speak('What would you like to write?')

                            while True:
                                with sr.Microphone() as source:
                                    print('Listening')
                                    speak('Listening')
                                    listener.pause_threshold = 2
                                    try:
                                        input_speech = listener.listen(source, timeout=10)
                                        print('Recognizing speech...')
                                        writeCommand = listener.recognize_google(input_speech, language='en_gb')
                                        print(f'The input speech was: {writeCommand}')

                                        # Check if the user wants to stop typing
                                        if writeCommand.lower() == 'stop typing':
                                            speak('Exiting typing mode.')
                                            break  # Exit the loop and typing mode

                                        pyautogui.write(writeCommand, interval=0.1)

                                    except sr.UnknownValueError:
                                        print('Sorry, I did not catch that')
                                        speak('Sorry, I did not catch that')
                                    except Exception as exception:
                                        print(f'An error occurred: {exception}')
                                        speak('An error occurred. Please try again.')

                        elif appControl == 'save':                            
                            pyautogui.hotkey('ctrl', 's')
                            time.sleep(2)
                            listener = sr.Recognizer()
                            speak('What would you like to name the file?')

                            while True:
                                with sr.Microphone() as source:
                                    print('Listening')
                                    speak('Listening')
                                    listener.pause_threshold = 2
                                    try:
                                        input_speech = listener.listen(source, timeout=10)
                                        print('Recognizing speech...')
                                        fileName = listener.recognize_google(input_speech, language='en_gb')
                                        print(f'The input speech was: {fileName}')
                                        pyautogui.write(fileName, interval = 0.1)
                                        pyautogui.hotkey('enter')
                                        time.sleep(2)
                                        pyautogui.hotkey('enter')
                                        break

                                    except sr.UnknownValueError:
                                        print('Sorry, I did not catch that')
                                        speak('Sorry, I did not catch that')
                                    except Exception as exception:
                                        print(f'An error occurred: {exception}')
                                        speak('An error occurred. Please try again.')

                        elif appControl == 'press enter':
                            for key in ['enter']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'select':
                            for key in ['tab']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'up':
                            for key in ['up']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'down':
                            for key in ['down']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'left':
                            for key in ['left']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'right':
                            for key in ['right']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'page up':
                            for key in ['pageup']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'page down':
                            for key in ['pagedown']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'play':
                            for key in ['playpause']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'pause':
                            for key in ['playpause']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'lower volume':
                            x = 0
                            while x<=10:
                                for key in ['volumedown']:
                                    pyautogui.press(key)
                                    x+=1
                                    if x>10:
                                        break
                        
                        elif appControl == 'higher volume':
                            while x<=10:
                                for key in ['volumeup']:
                                    pyautogui.press(key)
                                    x+=1
                                    if x>10:
                                        break

                        elif appControl == 'mute':
                            for key in ['volumemute']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'exit':
                            break

                        else:
                            speak('Sorry, I did not catch that')

                    except Exception as exception:
                        print('Sorry, I did not catch that')
                        speak('Sorry, I did not catch that')
                        print(exception)
                    