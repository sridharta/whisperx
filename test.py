import requests

api_key = "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"

url = "https://api.runpod.ai/v2/whisper/runsync"

# Set the API endpoint URL and audio file path
endpoint_url = 'https://api.whisper.ai/speech-to-text/v1/transcriptions'
audio_file_path = './121326.mp3'

# Set the request headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'audio/wav',
    'Accept-Language': 'en-US'
}

# Send the audio file in the request body and wait for the response
with open(audio_file_path, 'rb') as audio_file:
    response = requests.post(endpoint_url, headers=headers, data=audio_file)

# Parse the JSON response and print the transcription results
if response.status_code == 200:
    results = response.json()['results']
    for result in results:
        transcript = result['transcript']
        print(transcript)
else:
    print(f'Error: {response.status_code}')