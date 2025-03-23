This is a project that implements RAG with an Open-source model from Ollama to get context from the pokemon dataset and answer the questions.

The UI for this is done using Stremlit.

# Steps
## Data Finding and Processing:
- The data is gathered from https://www.gigasheet.com/sample-data/pokemon-data[Gigasheet].
- The preprocessing file converts the indivdual records into documents and is saved for reference into pokemon_documents.txt

## Approach of Implementation
1. Retrieval: How Documents Are Fetched
- Step 1: Embedding the Documents
Each document in your dataset (e.g., Pokémon descriptions) is converted into a vector embedding using a Sentence Transformers model (e.g., all-MiniLM-L6-v2).

Embeddings are numerical representations of text that capture semantic meaning. For example:

Document: `"Name: Bulbasaur, Type: Grass/Poison"`

Embedding: `[0.12, -0.45, 0.78, ..., 0.34]` (a 384-dimensional vector).

- Step 2: Building the FAISS Index
All document embeddings are stored in a FAISS index, which is optimized for fast similarity search.

FAISS organizes the embeddings in a way that allows it to quickly find the most similar vectors to a given query vector.

- Step 3: Embedding the Query
When a user asks a question (e.g., "What type is Bulbasaur?"), the query is also converted into an embedding using the same Sentence Transformers model.

Query: `"What type is Bulbasaur?"`

Query Embedding: `[0.15, -0.40, 0.75, ..., 0.30]`.

- Step 4: Similarity Search
FAISS compares the query embedding to all document embeddings in the index.

It calculates the cosine similarity (or Euclidean distance) between the query vector and each document vector.

The documents with the highest similarity scores are returned as the most relevant results.

Example
Query: `"What type is Bulbasaur?"`

FAISS finds that the document for Bulbasaur has the highest similarity score.

The top-k documents (e.g., top 3) are returned as the retrieved results.

2. Context Usage: How the LLM Uses Retrieved Documents
- Step 1: Formatting the Context
The retrieved documents are concatenated into a single string, which serves as the context for the LLM.

- Step 2: Generating the Answer
The LLM (e.g., Ollama with Llama 2) is prompted with the user’s query and the retrieved context.

The prompt instructs the LLM to answer the question based on the provided context.

- Step 3: LLM Generates the Answer
The LLM reads the context and generates an answer based on the information it contains.

For example:

Context: `"Name: Bulbasaur, Type 1: Grass, Type 2: Poison"`

Answer: `"Bulbasaur is a Grass and Poison type Pokémon."`