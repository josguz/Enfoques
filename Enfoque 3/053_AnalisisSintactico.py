
class Parser:
    def __init__(self):
        self.tokens = []

    def parse(self, expression):
        self.tokens = expression.replace(" ", "").split("")
        self.current_token = 0
        return self.expression()

    def expression(self):
        result = self.term()
        while self.current_token < len(self.tokens) and self.tokens[self.current_token] in ('+', '-'):
            operator = self.tokens[self.current_token]
            self.current_token += 1
            result = (operator, result, self.term())
        return result

    def term(self):
        result = self.factor()
        while self.current_token < len(self.tokens) and self.tokens[self.current_token] in ('*', '/'):
            operator = self.tokens[self.current_token]
            self.current_token += 1
            result = (operator, result, self.factor())
        return result

    def factor(self):
        token = self.tokens[self.current_token]
        self.current_token += 1
        if token.isdigit():
            return int(token)
        raise ValueError("Token inválido")


# Crear un analizador sintáctico
parser = Parser()
expression = "3 + 5 * (2 - 8)"
parsed_expression = parser.parse(expression)
print("Árbol sintáctico:", parsed_expression)
