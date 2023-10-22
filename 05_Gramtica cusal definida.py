# Definición de la gramática causal
# CausalStatement -> Action "causa" Effect
# Action -> "tocar" Instrument "con" Finger
# Instrument -> "guitarra" | "piano" | "violín"
# Finger -> "dedos" | "plectrum"
# Effect -> "sonido" "agudo" | "melodía" | "armonía"

# Funciones para analizar la gramática causal
def parse_action(tokens):
    if tokens[0] == "tocar" and tokens[2] == "con":
        return f"{tokens[0]} {tokens[1]} {tokens[2]} {tokens[3]}"

def parse_instrument(tokens):
    return tokens[0]

def parse_finger(tokens):
    return tokens[0]

def parse_effect(tokens):
    if tokens[0] == "sonido" and tokens[1] == "agudo":
        return "sonido agudo"
    else:
        return tokens[0]

def parse_causal_statement(tokens):
    action = parse_action(tokens[0:4])
    effect = parse_effect(tokens[4:])
    return f"{action} causa {effect}"

# Ejemplo de uso
input_statement = "tocar guitarra con dedos causa sonido agudo"
tokens = input_statement.split()
result = parse_causal_statement(tokens)
print("Resultado del análisis sintáctico:", result)
