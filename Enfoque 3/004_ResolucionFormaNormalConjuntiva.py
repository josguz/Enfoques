
from sympy.logic.boolalg import to_cnf
from sympy import symbols

# Definir variables lógicas
A, B, C = symbols('A B C')

# Ejemplo de expresión lógica
expression = (A & B) | (~A & C)  # A y B o no A y C

# Convertir a forma normal conjuntiva (FNC)
cnf_expression = to_cnf(expression, True)

# Mostrar la expresión original y la FNC
print("Expresión original:", expression)
print("Expresión en Forma Normal Conjuntiva (FNC):", cnf_expression)
