import streamlit as st
from retriever import retrieve
from generator import generate_answer
from pokeapi import fetch_pokemon_image, extract_pokemon_names, display_pokemon_images

# Disable Streamlit's module inspection for torch
import os
os.environ["STREAMLIT_SERVER_ENABLE_STATIC_FILE_HANDLING"] = "false"

# Load documents
def load_documents(file_path):
    with open(file_path, "r") as f:
        documents = f.read().split("\n\n")
    return documents

documents = load_documents("pokemon_documents.txt")

# Streamlit UI
st.title("PokéStop: Pokémon Knowledge Explorer")

# Input query
query = st.text_input("Ask a question about Pokémon:")

if query:
    try:
        # Retrieve relevant documents
        retrieved_docs = retrieve(query)
        
        # Generate answer using Ollama
        context = "\n".join(retrieved_docs)
        answer = generate_answer(query, context)
        
        # Display the answer
        st.subheader("Generated Answer:")
        st.write(answer)
        
        # Extract Pokémon names from the answer
        pokemon_names = extract_pokemon_names(answer)
        if pokemon_names:
            st.subheader("Related Pokémon:")
            display_pokemon_images(pokemon_names)
        else:
            st.warning("No Pokémon names found in the answer.")
        
        # Display retrieved documents in a scrollable section
        st.subheader("Retrieved Information:")
        retrieved_info = "\n\n".join(retrieved_docs)
        st.text_area("Retrieved Documents", retrieved_info, height=300)  # Scrollable text area
        
    except Exception as e:
        st.error(f"An error occurred: {e}")