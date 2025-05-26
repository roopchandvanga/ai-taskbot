import whisper, os

import os
import whisper

model = whisper.load_model("base")

def listen():
    print("🎤 Recording...")
    # Record 5 seconds of audio using ffmpeg
    os.system("ffmpeg -f dshow -i audio=\"Microphone (Realtek Audio)\" -t 5 output.wav")
    result = model.transcribe("audio.wav")
    print("🗣️ You said:", result["text"])
    return result["text"]
