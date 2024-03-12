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
    subscription_key = 'edbf4e1e76a74812a8bbe8db38e59678'
    region = 'uksouth'
    endpoint_id = 'c55e3bc9-4ff2-4d13-b74b-c29249653a79'

    # Call the function for live transcription from microphone input
    transcribe_live_audio(subscription_key, region, endpoint_id)