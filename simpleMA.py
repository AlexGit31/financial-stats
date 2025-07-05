import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Analyse des variations de prix avec moyenne mobile")

# Sélection du fichier CSV dans le dossier './data'
data_files = [f for f in os.listdir("./data") if f.endswith(".csv")]
selected_file = st.selectbox("Sélectionnez un fichier de données", data_files)


# Chargement des données sélectionnées
def load_data(file_path):
    data = pd.read_csv(file_path)
    if "Price" not in data.columns:
        st.error("Le fichier CSV doit contenir une colonne 'Price'.")
        return None
    data["Close"] = data["Price"]  # Renommer pour cohérence
    return data


data = load_data(f"./data/{selected_file}")

if data is not None:
    # Paramètres interactifs
    ma_period = st.slider("Période de la moyenne mobile", 5, 100, 20)
    consecutive_days = st.slider(
        "Nombre de jours consécutifs au-dessus de la MA", 1, 20, 6
    )
    future_days = st.slider("Nombre de jours pour observer les variations", 1, 30, 5)

    # Calcul de la moyenne mobile
    data["MA"] = data["Close"].rolling(window=ma_period).mean()
    data.dropna(subset=["MA"], inplace=True)

    # Identifier les périodes de jours consécutifs au-dessus de la moyenne mobile
    data["Above_MA"] = data["Close"] > data["MA"]
    data["Signal"] = (
        data["Above_MA"]
        .rolling(window=consecutive_days)
        .apply(lambda x: all(x), raw=True)
    )

    # Calculer les variations maximales
    variations = []
    for i in range(len(data) - future_days):
        if data["Signal"].iloc[i] == 1:
            future_prices = data["Close"].iloc[i + 1 : i + 1 + future_days]
            max_var = (future_prices.max() - data["Close"].iloc[i]) / data[
                "Close"
            ].iloc[i]
            min_var = (future_prices.min() - data["Close"].iloc[i]) / data[
                "Close"
            ].iloc[i]
            variations.append(max(max_var, min_var, key=abs))

    # Afficher l'histogramme
    st.subheader("Distribution des variations")
    fig, ax = plt.subplots()
    ax.hist(variations, bins=50, color="blue", edgecolor="black", alpha=0.7)
    ax.set_title("Distribution des variations maximales")
    ax.set_xlabel("Variation (%)")
    ax.set_ylabel("Fréquence")
    st.pyplot(fig)
