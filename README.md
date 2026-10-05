# Voice-to-Text Transcription Tool

A simple Python-based tool that uses the `SpeechRecognition` library and Google Web Speech API to transcribe audio files (WAV, AIFF, or FLAC) into text.

## Features
- Transcribe audio files to text via CLI.
- Supports common audio formats.
- Powered by Google Web Speech API.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tool:
   ```bash
   python transcription_tool.py path/to/your/audio.wav
   ```

## Dependencies
- `SpeechRecognition`
- `PyAudio` (optional, for microphone support)