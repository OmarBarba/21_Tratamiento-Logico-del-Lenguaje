import re

# Conjunto de datos de ejemplo
data = [
    "Is the sky blue?",
    "Are you coming to the party?",
    "What is your name?",
    "Have you finished your homework?",
    "How did you solve the problem?"
]

# Expresiones regulares para patrones comunes en preguntas en inglés
question_patterns = {
    "yes_no": r"(Is|Are|Have|Do) .+\?",
    "wh_question": r"(What|When|Where|Why|How) .+\?"
}

# Realiza la inducción gramatical
def induct_grammar(data, patterns):
    grammar = {}
    for sentence in data:
        for pattern_name, pattern in patterns.items():
            if re.match(pattern, sentence):
                if pattern_name not in grammar:
                    grammar[pattern_name] = [sentence]
                else:
                    grammar[pattern_name].append(sentence)
    return grammar

# Aplica la inducción gramatical al conjunto de datos
learned_grammar = induct_grammar(data, question_patterns)

# Muestra las reglas gramaticales aprendidas
for pattern, sentences in learned_grammar.items():
    print(f"Regla gramatical ({pattern}):")
    for sentence in sentences:
        print(f"  - {sentence}")
