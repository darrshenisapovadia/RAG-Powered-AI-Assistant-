# RAG-Based AI Assistant

This project converts video recordings into a searchable, AI-powered knowledge system using a Retrieval-Augmented Generation (RAG) pipeline.

It allows you to transcribe videos, generate vector embeddings from the content, and query the data using a Large Language Model (LLM) that provides answers grounded strictly in your own recordings.

---

## What This Project Does

Once your data is processed, you can ask questions such as:
- Where was a specific topic mentioned?
- Which video and timestamp discusses a particular concept?
- Summarize all content related to a given topic.

The system retrieves the most relevant transcript segments using vector similarity search and generates accurate, context-aware responses using an LLM.

---

## Project Workflow Overview

Videos → Audio → Transcripts → Embeddings → RAG Querying → AI Answers

---

## How to Use This Project

### Step 1 — Add Video Files

Place all raw video recordings inside the `videos/` directory.


---

### Step 2 — Convert Video to Audio (MP3)

Run the video-to-audio conversion script:

```bash
python process_video.py
```

This step:
- Scans the `videos/` directory
- Converts each video file into an MP3
- Saves outputs to the `audios/` directory
- Preserves naming structure for traceability

Processing audio instead of video significantly improves transcription speed and efficiency.

---

### Step 3 — Generate Transcripts (MP3 to JSON)

Convert audio files into structured transcript chunks:

```bash
python create_chunks.py
```

Each generated JSON file contains:
- Timestamped text segments
- Video number and title metadata
- Cleaned, translated transcript text

The `jsons/` directory will now contain text-based versions of all recordings.

---

### Step 4 — Create Vector Embeddings

Generate embeddings from transcript chunks:

```bash
python read_chunks.py
```

This step produces:
- A dataframe containing text chunks, timestamps, metadata, and embeddings
- A serialized embedding index stored as `embeddings.joblib`

These embeddings enable semantic search across your entire video dataset.

---

### Step 5 — Query the System (RAG Inference)

Ask questions using the retrieval and generation pipeline:

```bash
python process_incoming.py
```

The system will:
- Embed the user query
- Retrieve the most relevant transcript chunks using cosine similarity
- Build a context-rich prompt
- Generate a grounded answer using the LLM

Example questions:
- Where is topic X discussed?
- Summarize all content related to Y
- Identify videos and timestamps where Z appears

---

## Output Files

- `embeddings.joblib` – Vector embedding index
- `prompt.txt` – Prompt sent to the LLM
- `response.txt` – Final generated answer

---

## Tips for Best Results

- Use clear, noise-free audio recordings
- Keep filenames descriptive and consistent
- Re-run the embedding step when new files are added
- Maintain the expected directory structure

---

## Use Cases

- Course and lecture search
- Meeting and interview analysis
- Podcast and video content indexing
- Personal knowledge bases built from recordings
