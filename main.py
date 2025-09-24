# main.py
import streamlit as st

# Titre de la page
st.set_page_config(page_title="Ma première app Streamlit", layout="centered")

st.title("Bienvenue dans mon app Streamlit 🎈")
st.write("Ceci est une page simple en Streamlit avec quelques interactions de base.")

# Zone de saisie
nom = st.text_input("Quel est ton nom ?", "")

# Sélecteur
option = st.selectbox(
    "Choisis une option :",
    ["Option A", "Option B", "Option C"]
)

# Slider
valeur = st.slider("Choisis une valeur :", 0, 100, 50)

# Bouton
if st.button("Confirmer"):
    if nom:
        st.success(f"Salut {nom} 👋, tu as choisi **{option}** avec la valeur {valeur}.")
    else:
        st.warning("Entre ton nom avant de confirmer.")
