import whisper, os

import os
import whisper

model = whisper.load_model("base")

def listen():
    print("Recording...")
    # Record 5 seconds of audio using ffmpeg
    os.system("ffmpeg -y -f dshow -i audio=\"Microphone (Realtek(R) Audio)\" -t 5 audio.wav")
    result = model.transcribe("audio.wav")
    print("You said:", result["text"])
    return result["text"]
