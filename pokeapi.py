import requests
import ollama
from PIL import Image
from io import BytesIO
import streamlit as st


def fetch_pokemon_image(pokemon_name):
    """
    Fetch the official artwork of a Pokémon from PokéAPI.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
        return image_url
    return None

def display_pokemon_images(names):
    """
    Display Pokémon images in a grid layout.
    """
    cols = st.columns(3)  # Adjust the number of columns as needed
    for i, name in enumerate(names):
        image_url = fetch_pokemon_image(name)
        if image_url:
            with cols[i % 3]:  # Distribute images across columns
                st.image(image_url, caption=name, width=150)
        else:
            st.warning(f"Could not fetch image for {name}.")

def extract_pokemon_names(answer):
    """
    Use the LLM to extract Pokémon names from the generated answer.
    """
    prompt = f"""
    Extract the names of all Pokémon mentioned in the following text. Return them as a comma-separated list.

    Text: {answer}

    Example:
    Input: "Bulbasaur is a Grass and Poison type Pokémon. It evolves into Ivysaur and Venusaur."
    Output: Bulbasaur, Ivysaur, Venusaur
    """
    response = ollama.generate(model="mistral:latest", prompt=prompt)
    names = response["response"].strip().split(", ")
    return names