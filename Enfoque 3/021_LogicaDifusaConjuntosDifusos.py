
import numpy as np
import matplotlib.pyplot as plt

# Definición de un conjunto difuso
class FuzzySet:
    def __init__(self, name, membership_function):
        self.name = name
        self.membership_function = membership_function

    def membership(self, x):
        return self.membership_function(x)

# Ejemplo de función de membresía para un conjunto difuso "alto"
def tall_membership(x):
    return max(0, min(1, (x - 170) / 30))  # Altura en cm

# Crear un conjunto difuso para "alto"
tall_set = FuzzySet("Alto", tall_membership)

# Evaluar el conjunto difuso para diferentes alturas
heights = np.arange(140, 210, 1)
memberships = [tall_set.membership(h) for h in heights]

# Visualizar el conjunto difuso
plt.figure(figsize=(8, 4))
plt.plot(heights, memberships, label='Conjunto Difuso: Alto', color='blue')
plt.title('Función de Membresía del Conjunto Difuso')
plt.xlabel('Altura (cm)')
plt.ylabel('Grado de Membresía')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
