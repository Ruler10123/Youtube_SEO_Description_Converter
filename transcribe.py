import whisper
import os

model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])