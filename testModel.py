import azure.cognitiveservices.speech as speechsdk
import requests

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

def search_online(query, api_key, cx):
    # Define the Google Custom Search API endpoint
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&safe=high"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        search_results = response.json()
        # Extract search items from the response
        items = search_results.get("items", [])
        # Print search results
        for item in items:
            print("Title:", item.get("title"))
            print("Link:", item.get("link"))
            print("Snippet:", item.get("snippet"))
            print()
    else:
        print("Error occurred while performing search. Status code:", response.status_code)


if __name__ == "__main__":
    subscription_key = 'edbf4e1e76a74812a8bbe8db38e59678'
    region = 'uksouth'
    endpoint_id = 'c55e3bc9-4ff2-4d13-b74b-c29249653a79'

    # Call the function for live transcription from microphone input
    transcribe_live_audio(subscription_key, region, endpoint_id)

    query = input("Enter search query: ")
    api_key = 'AIzaSyCV3KiOM3FUTzTy64tTqdnWs7YO7ZzCBhI'
    cx = '72582d076697249f1'

    # Call the function to perform online search
    search_online(query, api_key, cx)