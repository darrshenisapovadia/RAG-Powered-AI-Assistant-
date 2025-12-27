# Reads transcript chunks from JSON files and creates vector embeddings for RAG

import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Create embeddings using local Ollama embedding model
def create_embedding(text_list):
    
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


# Load all transcript JSON files
jsons = os.listdir("jsons")  
my_dicts = []
chunk_id = 0

# Generate embeddings for each chunk across all files
for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    # Generate embeddings for all chunks in the current file
    embeddings = create_embedding([c['text'] for c in content['chunks']])
       
    # Attach embeddings and chunk ids to metadata
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk) 

# Store everything in a dataframe for fast retrieval
df = pd.DataFrame.from_records(my_dicts)

# Save embedding index for later querying
joblib.dump(df, 'embeddings.joblib')
