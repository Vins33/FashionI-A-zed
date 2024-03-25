import pandas as pd
import webcolors

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_NAMES_TO_HEX.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(name)
        rd = (r_c - requested_color) ** 2
        gd = (g_c - requested_color) ** 2
        bd = (b_c - requested_color) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# Leggi il CSV
data = pd.read_csv('predictions.csv')

# Seleziona la colonna 'dominant_color' e applica la funzione 'closest_color'
data['dominant_colorhex'] = data['dominant_color'].apply(closest_color)

# Salva l'output nel file CSV originale
data.to_csv('predictions.csv', index=False)
