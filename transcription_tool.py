import speech_recognition as sr
import os
import sys

def transcribe_audio(file_path):
    """
    Transcribes the given audio file into text.
    """
    recognizer = sr.Recognizer()
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with sr.AudioFile(file_path) as source:
        print("Processing audio...")
        audio_data = recognizer.record(source)
        
        try:
            # Using Google Web Speech API (free, no API key required for basic use)
            text = recognizer.recognize_google(audio_data)
            print("Transcription:")
            print("-" * 20)
            print(text)
            print("-" * 20)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcription_tool.py <path_to_audio_file>")
    else:
        transcribe_audio(sys.argv[1])