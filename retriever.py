from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_documents(file_path):
    with open(file_path,'r') as f:
        documents = f.read().split('\n\n') # Split by double llines for new pokemon
    return documents

documents = load_documents('pokemon_documents.txt')

model = SentenceTransformer('all-MiniLM-L6-v2') # Retriever model

document_embeddings = model.encode(documents) # Encoding the documents

# Building the Faiss Index
dimension = document_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(document_embeddings)

def retrieve(query,top_k=3):
    querry_embedding = model.encode([query])
    distances,indices = index.search(querry_embedding,k=top_k)
    
    # Format retrieved documents
    formatted_docs = []
    for i in indices[0]:
        doc = documents[i]
        # Convert the document into key-value pairs
        formatted_doc = "\n".join([f"- {line.strip()}" for line in doc.split("\n") if line.strip()])
        formatted_docs.append(formatted_doc)
    
    return formatted_docs

