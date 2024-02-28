import azure.cognitiveservices.speech as speechsdk

def transcribe_live_audio(subscription_key, region, endpoint_id):
    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.endpoint_id = endpoint_id

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into the microphone...")
    # Start continuous recognition
    result = speech_recognizer.recognize_once()

    # Check if the transcription was successful
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Transcription:", result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled:", cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details:", cancellation_details.error_details)

if __name__ == "__main__":
    subscription_key = 'acc78bfd447a4a838dd4f31f3de95a7e'
    region = 'westeurope'
    endpoint_id = 'e6fa38b2-d6a3-4ca6-a120-45877d9be4db'

    # Call the function for live transcription from microphone input
    transcribe_live_audio(subscription_key, region, endpoint_id)