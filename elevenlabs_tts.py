import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_audio(text, voice="default"):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    url = "https://api.elevenlabs.io/v1/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice": voice
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        print("Audio generated and saved as output.mp3")
    else:
        print(f"Error: {response.text}")
