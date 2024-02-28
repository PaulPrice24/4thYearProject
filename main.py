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
import azure.cognitiveservices.speech as speechsdk
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
    subscription_key = 'acc78bfd447a4a838dd4f31f3de95a7e'
    region = 'westeurope'
    endpoint_id = 'e6fa38b2-d6a3-4ca6-a120-45877d9be4db'

    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.endpoint_id = endpoint_id

    listener = speechsdk.SpeechRecognizer(speech_config=speech_config)

    with sr.Microphone() as source:
        print('Listening')
        speak('Listening')
        # Create a speech recognizer
        result = listener.recognize_once()
        result.pause_threshold = 2

    try:
        print('Recognizing speech...')
        query = result.text
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

        query[0] = query[0].rstrip('.!?')

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
            
            if query[0] == 'play' and query[1] == 'music.':
                    subscription_key = 'acc78bfd447a4a838dd4f31f3de95a7e'
                    region = 'westeurope'
                    endpoint_id = 'e6fa38b2-d6a3-4ca6-a120-45877d9be4db'

                    # Set up the speech configuration
                    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
                    speech_config.endpoint_id = endpoint_id

                    listener = speechsdk.SpeechRecognizer(speech_config=speech_config)

                    with sr.Microphone() as source:
                        print('What would you like to play?')
                        speak('What would you like to play?')
                        # Create a speech recognizer
                        result = listener.recognize_once()
                        result.pause_threshold = 2
                        song = result.text
                
                        print(f'Playing {song}')

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

            if query[0] == 'what' and query[1] == 'time' and query[2] == 'is' and query[3] == 'it?':
                speech = datetime.datetime.now().strftime("%H:%M")
                speak(speech)

            if query[0] == 'what' and query[1] == 'is' and query[2] == 'the' and query[3] == 'time?':
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

            if query[0] == 'exit.':
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

                window_title = window_title.rstrip('.!?')

                # Close Word window
                word_window = gw.getWindowsWithTitle(window_title)
                if word_window:
                    word_window[0].close()
                    time.sleep(2)  # Add a delay to allow time for the window to close
                else:
                    print(f"Window with title '{window_title}' not found.")

            if query[0] == 'keyboard.':
                query.pop(0)
                
                x = 1

                while x == 1:
                    speak('Keyboard Control enabled')

                    subscription_key = 'acc78bfd447a4a838dd4f31f3de95a7e'
                    region = 'westeurope'
                    endpoint_id = 'e6fa38b2-d6a3-4ca6-a120-45877d9be4db'

                    # Set up the speech configuration
                    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
                    speech_config.endpoint_id = endpoint_id

                    listener = speechsdk.SpeechRecognizer(speech_config=speech_config)

                    speak("Listening")

                    with sr.Microphone() as source:
                        # Create a speech recognizer
                        result = listener.recognize_once()
                        result.pause_threshold = 2
                        appControl = result.text

                    try:
                        print('Recognizing speech...')
                        print(f'The input speech was: {appControl}')

                        if appControl == 'Search.':
                            pyautogui.hotkey('ctrl', 'l')
                            
                        elif appControl == 'Enable typing.':
                            speak('What would you like to write?')

                            while True:
                                subscription_key = 'acc78bfd447a4a838dd4f31f3de95a7e'
                                region = 'westeurope'
                                endpoint_id = 'e6fa38b2-d6a3-4ca6-a120-45877d9be4db'

                                # Set up the speech configuration
                                speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
                                speech_config.endpoint_id = endpoint_id

                                listener = speechsdk.SpeechRecognizer(speech_config=speech_config)

                                with sr.Microphone() as source:
                                    # Create a speech recognizer
                                    result = listener.recognize_once()
                                    result.pause_threshold = 2
                                    writeCommand = result.text

                                    # Check if the user wants to stop typing
                                    if writeCommand.lower() == 'Stop typing.':
                                        speak('Exiting typing mode.')
                                        break  # Exit the loop and typing mode
                                    elif writeCommand.lower() == 'Stop typing':
                                        speak('Exiting typing mode.')
                                        break  # Exit the loop and typing mode
                                    elif writeCommand.lower() == 'Stop Typing.':
                                        speak('Exiting typing mode.')
                                        break  # Exit the loop and typing mode
                                    elif writeCommand.lower() == 'stop typing.':
                                        speak('Exiting typing mode.')
                                        break  # Exit the loop and typing mode
                                    elif writeCommand.lower() == 'stop typing':
                                        speak('Exiting typing mode.')
                                        break  # Exit the loop and typing mode
                                    else:
                                        pyautogui.write(writeCommand, interval=0.1)

                        elif appControl == 'Save.':                            
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

                        elif appControl == 'Press Enter.':
                            for key in ['enter']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'Select.':
                            for key in ['tab']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Up.':
                            for key in ['up']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Down.':
                            for key in ['down']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'Left.':
                            for key in ['left']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Right.':
                            for key in ['right']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Page up.':
                            for key in ['pageup']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'Page down.':
                            for key in ['pagedown']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Play.':
                            for key in ['playpause']:
                                time.sleep(2)
                                pyautogui.press(key)
                        
                        elif appControl == 'Pause.':
                            for key in ['playpause']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Lower volume.':
                            x = 0
                            while x<=10:
                                for key in ['volumedown']:
                                    pyautogui.press(key)
                                    x+=1
                                    if x>10:
                                        break
                        
                        elif appControl == 'Higher volume.':
                            while x<=10:
                                for key in ['volumeup']:
                                    pyautogui.press(key)
                                    x+=1
                                    if x>10:
                                        break

                        elif appControl == 'Mute.':
                            for key in ['volumemute']:
                                time.sleep(2)
                                pyautogui.press(key)

                        elif appControl == 'Exit.':
                            break

                        else:
                            speak('Sorry, I did not catch that')

                    except Exception as exception:
                        print('Sorry, I did not catch that')
                        speak('Sorry, I did not catch that')
                        print(exception)
                    