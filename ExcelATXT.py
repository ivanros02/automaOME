import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('reporte_pacientes.xlsx')

# Mostrar opciones al usuario
print("Por favor, elija una de las siguientes opciones:")
print("1. 520101")
print("2. 0")
print("3. 521001") 

# Pedir al usuario que elija una opción
opcion = input("Ingrese el número de la opción deseada: ")

# Verificar la opción elegida y filtrar el DataFrame en consecuencia
if opcion == "1":
    codigo = 520101
elif opcion == "2":
    codigo = 0
elif opcion == "3":
    codigo = 521001
else:
    print("Opción no válida.")
    exit()

# Filtrar el DataFrame por el código seleccionado en la columna 'Código de Práctica'
df_filtrado = df[df['Código de Práctica'] == codigo]

# Seleccionar las columnas 'Beneficio' y 'Código de Diagnóstico' del DataFrame filtrado
columnas_seleccionadas = df_filtrado[['Beneficio', 'Código de Diagnóstico']]

# Guardar las columnas seleccionadas en un archivo CSV sin incluir el nombre de las columnas
columnas_seleccionadas.to_csv('aRealizar.txt', index=False, header=False)

