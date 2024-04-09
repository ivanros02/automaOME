datos = '''
F429
F009
F419
F41.3
F41
F22
F41
F20.0
F33
F41.9
F41.2
F41.9
F43.9
F32.2
F41.9
F32.1
F41.2
F41.9
'''

# Eliminar los puntos de las cadenas
datos_sin_puntos = datos.replace('.', '')

print(datos_sin_puntos)
