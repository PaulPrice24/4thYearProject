import os
import sys
from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
import pygame

def translate_language(sentence, dest_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(sentence, dest=dest_language)
    return translation.text

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
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

    pygame.mixer.init()

    while True:
        try:
            user_input = recognize_speech()
            if user_input:
                if user_input == "exit":
                    break
                else:
                    translated_sentence = translate_language(user_input, dest_language)
                    print(f"{translated_sentence}")
                    voice = gTTS(translated_sentence, lang=v1)
                    voice.save("voice.mp3")
                    pygame.mixer.Sound("voice.mp3").play()
                    os.remove("voice.mp3")  # Remove the sound file after playing
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()