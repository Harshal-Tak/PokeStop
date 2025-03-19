import streamlit as st
from retriever import retrieve
from generator import generate_answer

import os
os.environ["STREAMLIT_SERVER_ENABLE_STATIC_FILE_HANDLING"] = "false"

st.title('PokeStop - One Stop Desitnation for Pokemon')

query = st.text_input("Ask question related to Pokemon: ")

if query:
    try:
        # Retrieve relevant documents
        st.subheader("Retrieved Information: ")
        retrieved_docs = retrieve(query)
        for doc in  retrieved_docs:
            st.write(doc)

        # Amser throught Ollama
        st.subheader("Generated Answer: ")
        context = "\n".join(retrieved_docs)
        answer = generate_answer(query,context)
        st.write(answer)

    except Exception as e:
        st.error(f"An error occurred: {e}")

