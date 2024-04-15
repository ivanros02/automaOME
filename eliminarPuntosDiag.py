# Abrir el archivo en modo lectura
with open('beneficios13.04.txt', 'r') as file:
    # Leer el contenido del archivo
    data = file.read()

# Reemplazar los puntos por una cadena vacía
data_sin_puntos = data.replace('.', '')

# Abrir el archivo en modo escritura y escribir el contenido sin puntos
with open('beneficios13.04.txt', 'w') as file:
    file.write(data_sin_puntos)
