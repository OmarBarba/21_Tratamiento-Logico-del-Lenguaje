class SyntaxAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def parse(self):
        try:
            self.expression()
            if self.index == len(self.input_string):
                print("Análisis sintáctico exitoso: La expresión es válida.")
            else:
                print("Error sintáctico: La expresión no es válida.")
        except Exception as e:
            print(f"Error sintáctico: {str(e)}")

    def match(self, char):
        if self.index < len(self.input_string) and self.input_string[self.index] == char:
            self.index += 1
        else:
            raise Exception(f"Se esperaba '{char}' en posición {self.index}.")

    def factor(self):
        if self.input_string[self.index] == '(':
            self.match('(')
            self.expression()
            self.match(')')
        else:
            self.number()

    def number(self):
        if self.input_string[self.index].isdigit():
            self.match(self.input_string[self.index])
        else:
            raise Exception(f"Se esperaba un número en posición {self.index}.")

    def term(self):
        self.factor()
        while self.index < len(self.input_string) and self.input_string[self.index] == '*':
            self.match('*')
            self.factor()

    def expression(self):
        self.term()
        while self.index < len(self.input_string) and self.input_string[self.index] == '+':
            self.match('+')
            self.term()

# Uso del analizador sintáctico
input_string = "1*(2+3)+4"
analyzer = SyntaxAnalyzer(input_string)
analyzer.parse()
