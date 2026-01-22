
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función objetivo
def objective_function(x):
    return x**2 + 4 * np.sin(5 * x)

# Descenso del gradiente
def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    x_history = [x]
    
    for _ in range(num_iterations):
        grad = 2 * x + 20 * np.cos(5 * x)  # Gradiente de la función
        x -= learning_rate * grad  # Actualización
        x_history.append(x)
    
    return x, x_history

# Parámetros de la búsqueda
starting_point = 0.5
learning_rate = 0.01
num_iterations = 50

# Ejecución del descenso del gradiente
min_x, x_history = gradient_descent(starting_point, learning_rate, num_iterations)

# Visualización
x = np.linspace(-3, 3, 100)
y = objective_function(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Función Objetivo', color='blue')
plt.plot(x_history, objective_function(np.array(x_history)), 'ro-', label='Trayectoria del descenso')
plt.title('Algoritmo de Búsqueda Local: Descenso del Gradiente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

print(f"Valor mínimo encontrado en x = {min_x:.2f}")
