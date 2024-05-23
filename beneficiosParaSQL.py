# Nombre del archivo de texto
archivo = "resultadosACEPTACION.txt"

# Lista para almacenar los números
numeros = []

# Leer el archivo línea por línea
with open(archivo, "r") as f:
    for linea in f:
        # Dividir la línea por la coma y tomar el primer elemento
        numero = linea.split(",")[0]
        # Agregar el número a la lista
        numeros.append("'" + numero + "'")

# Imprimir los números en el formato deseado
print(", ".join(numeros))
