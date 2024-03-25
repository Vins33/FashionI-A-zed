import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titolo e sottotitolo
st.title('Il tuo titolo qui')
st.subheader('Il tuo sottotitolo qui')

# Percorso del file CSV
csv_path = 'predictions.csv'

# Leggi il CSV
data = pd.read_csv(csv_path)

# Crea un grafico
st.write("Grafico dei dati")
fig, ax = plt.subplots()
ax.scatter(data['predicted_labels'], data['dominant_color'])
ax.set_xlabel('predicted_labels')
ax.set_ylabel('dominant_color')
st.pyplot(fig)
