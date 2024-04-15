import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('omehoy.xlsx')

# Selecciona las columnas B, E y G
columnas_seleccionadas = df[['Beneficio', 'Código de Diagnóstico']]

# Guarda las columnas seleccionadas en un archivo CSV separado por comas
columnas_seleccionadas.to_csv('aRealizar.txt', index=False)
