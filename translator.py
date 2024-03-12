import os
import sys
from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
import azure.cognitiveservices.speech as speechsdk
import pygame

def translate_language(sentence, dest_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(sentence, dest=dest_language)
    return translation.text

def recognize_speech():
    subscription_key = 'edbf4e1e76a74812a8bbe8db38e59678'
    region = 'uksouth'
    endpoint_id = 'c55e3bc9-4ff2-4d13-b74b-c29249653a79'

    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.endpoint_id = endpoint_id

    listener = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print('Say something...')
    # Create a speech recognizer
    result = listener.recognize_once()

    try:
        user_input = result.text
        print(f"User said: {user_input}")
        return user_input.lower()
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print(f"Error with the speech recognition; {e}")

def main():
    if len(sys.argv) != 2:
        return

    dest_language = sys.argv[1].lower()
    v1 = ""

    if dest_language == "french":
        v1 = "fr"
    elif dest_language == "spanish":
        v1 = "es"
    elif dest_language == "german":
        v1 = "de"
    elif dest_language == "dutch":
        v1 = "nl"
    elif dest_language == "polish":
        v1 = "pl"
    elif dest_language == "portuguese":
        v1 = "pt"
    elif dest_language == "russian":
        v1 = "ru"
    elif dest_language == "italian":
        v1 = "it"

    pygame.mixer.init()

    audio_finished = True

    while True:
        try:
            if audio_finished:
                user_input = recognize_speech()
                if user_input:
                    if user_input == "exit.":
                        break
                    else:
                        translated_sentence = translate_language(user_input, dest_language)
                        print(f"{translated_sentence}")
                        voice = gTTS(translated_sentence, lang=v1)
                        voice.save("voice.mp3")
                        pygame.mixer.Sound("voice.mp3").play()
                        os.remove("voice.mp3")  # Remove the sound file after playing
                        audio_finished = False
            else:
                if not pygame.mixer.get_busy():
                    audio_finished = True
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()