# Percorso del file CSV
import pandas as pd

csv_path = 'predictions.csv'

# Leggi il CSV
data = pd.read_csv(csv_path)

# Sostituisci 'colonna' con il nome della tua colonna
colonna = 'predicted_labels'
dizionario = {
    0: 'sunglass',
    1: 'hat',
    2: 'jacket',
    3: 'shirt',
    4: 'pants',
    5: 'shorts',
    6: 'skirt',
    7: 'dress',
    8: 'bag',
    9: 'shoe',
}
# Per ogni riga nel DataFrame
for i in range(len(data)):
    # Prendi il valore nella colonna
    valore = data.loc[i, colonna]

    # Se il valore è nel dizionario
    if valore in dizionario:
        # Rimpiazza il valore nella colonna con il valore corrispondente nel dizionario
        data.loc[i, colonna] = dizionario[valore]
data.to_csv('predicitions.csv')
