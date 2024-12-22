from elevenlabs_tts import generate_audio
from twilio_call import make_call

if __name__ == "__main__":
    # Step 1: Generate audio
    text = "Hello, this is a test call using ElevenLabs and Twilio!"
    generate_audio(text)

    # Step 2: Make the outbound call
    recipient_number = "+12185015575"  # Replace with the recipient's phone number
    make_call(recipient_number)
