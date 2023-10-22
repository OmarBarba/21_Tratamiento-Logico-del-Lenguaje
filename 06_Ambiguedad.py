import ply.yacc as yacc

# Definición de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# Reglas de expresión regular para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Reglas de producción
def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expr RPAREN'''
    if len(p) == 2:
        p[0] = int(p[1])
    else:
        p[0] = p[2]

# Construye el analizador sintáctico
parser = yacc.yacc()

# Función para realizar el análisis sintáctico
def parse_expression(expression):
    return parser.parse(expression)

# Ejemplo de uso
input_expression = "1 + 2 * (3 - 4)"
result = parse_expression(input_expression)
print("Resultado del análisis sintáctico:", result)
