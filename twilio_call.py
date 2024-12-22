import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def make_call(to_number):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
    audio_url = os.getenv("PUBLIC_AUDIO_URL")

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        twiml=f'<Response><Play>{audio_url}</Play></Response>',
        to=to_number,
        from_=twilio_number
    )
    print(f"Call initiated with SID: {call.sid}")
