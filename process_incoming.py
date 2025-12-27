# Handles user queries using RAG: retrieve relevant chunks and generate answers via LLM

import pandas as pd  
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import joblib 
import requests


# Create embedding for user query using local embedding model
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


# Send prompt to LLM and get generated response
def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    print(response)
    return response


# Load precomputed embeddings dataframe
df = joblib.load('embeddings.joblib')


# Take user question as input
incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0] 


# Compute similarity between query and stored chunks
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_indx] 


# Build prompt using the most relevant video chunks
prompt = f'''I am teaching web development in my Sigma web development course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''

# Save prompt for debugging or reuse
with open("prompt.txt", "w") as f:
    f.write(prompt)


# Generate final answer using LLM
response = inference(prompt)["response"]
print(response)

# Darrsheni Sapovadia's project 

# Save response output
with open("response.txt", "w") as f:
    f.write(response)
