import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def translate_to_french(sentence):
    translator = Translator()
    translation = translator.translate(sentence, dest='fr')
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
    while True:
        try:
            user_input = recognize_speech()
            if user_input:
                if user_input == "exit":
                    break
                else:
                    translated_sentence = translate_to_french(user_input)
                    print(f"{translated_sentence}")
                    engine = pyttsx3.init()
                    engine.say(translated_sentence)
                    engine.runAndWait()

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()