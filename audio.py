import whisper
import os
import subprocess

def listen():
    model = whisper.load_model("base")
    mic_name = "Microphone (Realtek(R) Audio)" 

    print("Listening...")
    # remove FFmpeg output by redirecting it to null
    subprocess.run(
        ['ffmpeg', '-y', '-f', 'dshow', '-i', f'audio={mic_name}', '-t', '5', 'audio.wav'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("Stopped recording.")

    result = model.transcribe("audio.wav", verbose=False)
    print("You said:", result["text"].strip())
    return result["text"]
