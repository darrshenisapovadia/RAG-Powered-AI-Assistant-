🔊 RAG-Based Audio–Video Knowledge Extraction Assistant
Transform your own recordings into a searchable, intelligent AI knowledge system.

This project enables you to convert any set of videos into text, index them using vector embeddings, and query them through an LLM that retrieves information grounded in your data.

Once your dataset is processed, you can ask questions like:
- “Where was this specific topic mentioned?”
- “Which part talked about X?”
- “Summarize the key points related to Y.”

The assistant uses Retrieval-Augmented Generation (RAG) to find the most relevant segments from your files and generate accurate, context-aware answers.

📁 How to Use This Assistant on Your Own Data
Below is a clean, professional, and complete workflow.

✅ Step 1 — Add Your Video Files: Place all your raw video recordings inside the /videos directory.

Supported input formats: .mp4, .mov, .mkv,.avi

Tip: Use descriptive filenames so you can easily map AI responses back to original files later.

🎧 Step 2 — Extract Audio (Convert Video → MP3)

Run the conversion script:

python video_to_mp3.py

This step will:

Scan the /videos folder

Convert each video into an .mp3 file

Save all audio outputs insidethe /audio directory

Preserve naming structure for consistency

Why?
👉 Processing audio is significantly faster and more efficient for transcription and embedding.

📝 Step 3 — Generate Text Data (MP3 → JSON)

Use the transcription script to convert all audio files into structured JSON files:

python mp3_to_json.py


Each generated JSON file contains:

Cleaned transcript text

Timestamped segments

Structured grouping for downstream vectorization

Your /json folder will now contain text-based versions of all your recordings.

🧠 Step 4 — Create Vector Embeddings (JSON → Embedding Store)

Convert the JSON transcripts into vector embeddings using the preprocessing script:

python preprocess_json.py


This step generates:

A dataframe with:

Chunked text

Associated timestamps

Embedding vectors

Metadata fields

A Joblib (.pkl) file that stores your embedding index efficiently
(e.g., embeddings_store.pkl)

Why?
👉 These embeddings allow the system to search and retrieve exactly the portions of your dataset that relate to a user query.

🤖 Step 5 — Ask Questions Using the LLM (RAG Stage)

Load your embedding store:

from joblib import load
embeddings_df = load("embeddings_store.pkl")


Now the assistant will:

Take the user’s question

Retrieve the most relevant text chunks using similarity search

Construct a context-rich prompt

Send this prompt to the LLM

Return an accurate answer grounded in your original data

You can ask questions such as:
- “Where is X mentioned?”
- “Summarize all points related to Y.”
- “Find portions where Z is discussed.”
- “Give a structured explanation of everything related to Topic A.”

📊 End-to-End Workflow Overview: Videos → Audio → Text → Embeddings → RAG Querying → AI Answers

⚙️ Tips for Best Output Quality
Use clear audio for better transcription
Keep filenames descriptive
Re-run the embedding script whenever you add new files
Maintain a consistent directory structure
