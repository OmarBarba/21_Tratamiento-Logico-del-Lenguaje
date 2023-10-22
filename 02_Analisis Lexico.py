import re

def analisis_lexico(oracion):
    # Utilizamos expresiones regulares para dividir el texto en palabras
    palabras = re.findall(r'\b\w+\b', oracion)
    return palabras

# Oración de ejemplo
oracion = "El análisis léxico es el primer paso en PLN."

# Realizar el análisis léxico
tokens = analisis_lexico(oracion)

# Imprimir los tokens
for token in tokens:
    print(token)
