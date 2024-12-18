from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text, lang='en'):
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang)
        
        # Save the audio file
        audio_file = "speech.mp3"
        tts.save(audio_file)
        print(f"Audio file saved as {audio_file}")
        
        # Check if the file exists
        
        if os.path.exists(audio_file):
            # Play the audio file
            playsound(audio_file)
            print("Audio played successfully")
            
            # Optionally, remove the audio file after playing
            print("Audio file removed after playing")
        else:
            print(f"Error: The file {audio_file} was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    text = "Hello, this is a test of the Google Text-to-Speech library."
    text_to_speech(text)
