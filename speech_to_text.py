# Simple script to test Whisper transcription on a single audio file

import whisper
import json

# Load Whisper model
model = whisper.load_model("medium")

# Transcribe sample audio and translate to English
result = model.transcribe(audio= "audios/sample.mp3",
                          language="hi",
                          task="translate",
                          word_timestamps=False)

# Print raw segments for inspection
print(result["segments"])

# Create basic timestamped text chunks
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"],
                 "end": segment["end"],
                 "text": segment["text"]})
    

print(chunks)

# Save output to JSON file
with open("output.json", "w") as f:
    json.dump(chunks, f)

print("Saved to ouput.json")
