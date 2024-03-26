import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

csv = 'predicitions.csv'
@st.cache_data
def load_data(csv):
    # Carica i tuoi dati qui
    # Sto usando un DataFrame vuoto come esempio
    df = pd.read_csv(csv)
    return df

def create_chart(df):
    # Calcola il conteggio dei valori unici per 'dominant_color' e 'predicted_labels'
    df['combined'] = df['dominant_color'] + "/" + df['predicted_labels']
    count_df = df['combined'].value_counts().reset_index(name='counts')
    top_10 = count_df.nlargest(10, 'counts')
    # Crea un grafico a barre
    fig, ax = plt.subplots()
    ax.bar(top_10['combined'], top_10['counts'])
    ax.set_xlabel('Combined')
    ax.set_ylabel('Counts')
    plt.xticks(rotation=45)
    return fig

def main():
    df = load_data(csv)
    chart = create_chart(df)
    st.pyplot(chart)

if __name__ == "__main__":
    main()
