
# Definir una función de orden superior
def higher_order_predicate(func, value):
    return func(value)

# Definir un predicado simple
def is_even(n):
    return n % 2 == 0

# Usar la función de orden superior con el predicado
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if higher_order_predicate(is_even, n)]

print("Números pares:", even_numbers)
