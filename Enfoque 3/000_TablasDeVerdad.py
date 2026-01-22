
import itertools
import pandas as pd

# Función para evaluar la expresión lógica
def evaluate_expression(A, B):
    return (A and B) or (not A and not B)  # Ejemplo: Equivalencia lógica (A ↔ B)

# Generar las combinaciones de valores de verdad
variables = ['A', 'B']
values = list(itertools.product([True, False], repeat=len(variables)))

# Crear una tabla de verdad
table = []

for value in values:
    row = list(value)
    row.append(evaluate_expression(*value))  # Evaluar la expresión
    table.append(row)

# Convertir a DataFrame para mejor visualización
df = pd.DataFrame(table, columns=variables + ['Resultado'])
print(df)
