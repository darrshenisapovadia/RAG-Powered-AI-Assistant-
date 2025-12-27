# Transcribes audio files using Whisper and creates timestamped text chunks

import whisper 
import json
import os

# Load Whisper speech-to-text model
model = whisper.load_model("medium")

# Read all audio files from audios directory
audios = os.listdir("audios")

# Process each audio file
for audio in audios:
    if("_" in audio):

        # Extract video number and title from filename
        number = audio.split("_")[0]
        title = audio.split("_")[1]
        print(number, title)

        # Transcribe audio and translate to English
        result = model.transcribe(audio = f"audios/{audio}", language = "hi", task="translate", word_timestamp=False)

        # Store transcript in smaller timestamped chunks
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number,
                           "title": title,
                          "start": segment["start"],
                          "end": segment["end"],
                          "text": segment["text"]})
        
        # Placeholder for adding full-text metadata if needed later
        chunks_with_metadata = {chunks: chunks, "text": result["text"]}

        # Save chunks as JSON for downstream embedding
        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks,f)
