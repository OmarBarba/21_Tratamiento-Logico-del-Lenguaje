from lark import Lark, Transformer, v_args

# Definición de la gramática EBNF para expresiones matemáticas
grammar = """
    start: expression

    ?expression: term
        | expression "+" term -> add
        | expression "-" term -> subtract

    ?term: factor
        | term "*" factor -> multiply
        | term "/" factor -> divide

    ?factor: atom
        | "-" factor -> negate

    ?atom: NUMBER -> number
        | "(" expression ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

# Definición del analizador sintáctico
calc_parser = Lark(grammar, start="start")

# Clase Transformer para construir el árbol de análisis sintáctico
class CalcTreeBuilder(Transformer):
    @v_args(inline=True)
    def add(self, left, right):
        return ["+", left, right]

    @v_args(inline=True)
    def subtract(self, left, right):
        return ["-", left, right]

    @v_args(inline=True)
    def multiply(self, left, right):
        return ["*", left, right]

    @v_args(inline=True)
    def divide(self, left, right):
        return ["/", left, right]

    @v_args(inline=True)
    def negate(self, expr):
        return ["-", expr]

    @v_args(inline=True)
    def number(self, value):
        return float(value)

# Función para realizar el análisis sintáctico y construir el árbol
def parse_expression(expression):
    tree = calc_parser.parse(expression)
    tree_builder = CalcTreeBuilder()
    return tree_builder.transform(tree)

# Ejemplo de uso
expression = "1 + (2 * 3)"
parsed_tree = parse_expression(expression)
print("Árbol de análisis sintáctico:", parsed_tree)
