import ollama

def generate_answer(query, context):
    """
    Generate an answer using Ollama and the retrieved context.
    """
    prompt = f"""
    You are a Pokémon expert. Answer the following question based on the context provided.

    Question: {query}

    Context:
    {context}

    Instructions:
    - If the context contains the answer, provide a concise and accurate response.
    - If the context does not contain the answer, say "I don't know."
    """

    response = ollama.generate(model='llama3.1:latest',prompt=prompt)
    return response['response']
