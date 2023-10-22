def generar_gramatica(reglas):
    gramatica = ""
    for regla in reglas:
        gramatica += f"{regla[0]} -> {regla[1]}\n"
    return gramatica

def traducir_cadena(cadena, gramatica):
    traduccion = ""
    for simbolo in cadena:
        if simbolo in gramatica:
            traduccion += gramatica[simbolo]
        else:
            traduccion += simbolo
    return traduccion

# Gramática
gramatica = {
    'S': ['AS', 'S1S2', 'SS', 'VV'],
    'AS': ['S', 'AS', 'SS', 'VV'],
    'S1S2': ['S1', 'S1S2', 'SS', 'VV'],
    'SS': ['S', 'S'],
    'VV': ['V', 'V']
}

reglas = [(key, value[0]) for key, value in gramatica.items()]

gramatica_texto = generar_gramatica(reglas)
print(gramatica_texto)

cadena = "VV"
cadena_traducida = traducir_cadena(cadena, gramatica)
print(f"Cadena traducida: {cadena_traducida}")