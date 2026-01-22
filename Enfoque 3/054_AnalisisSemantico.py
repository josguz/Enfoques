
class SemanticAnalyzer:
    def __init__(self):
        self.variables = {}

    def analyze(self, statements):
        for statement in statements:
            self.evaluate(statement)

    def evaluate(self, statement):
        if '=' in statement:
            var_name, expression = statement.split('=')
            self.variables[var_name.strip()] = self.evaluate_expression(expression.strip())
        else:
            print("Evaluando expresión:", self.evaluate_expression(statement.strip()))

    def evaluate_expression(self, expression):
        # Evaluación simple (sólo suma de números en este ejemplo)
        parts = expression.split('+')
        return sum(int(part.strip()) for part in parts)

# Crear un analizador semántico
analyzer = SemanticAnalyzer()
statements = [
    "x = 3 + 5",
    "y = 10 + 2",
    "x + y"
]

# Realizar el análisis semántico
analyzer.analyze(statements)
# Mostrar las variables
print("Variables:", analyzer.variables)
