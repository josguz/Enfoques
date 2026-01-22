
import numpy as np
import matplotlib.pyplot as plt

# Distribución Normal
media, desviacion = 0, 1
datos_normal = np.random.normal(media, desviacion, 1000)

# Distribución Binomial
n, p = 10, 0.5
datos_binomial = np.random.binomial(n, p, 1000)

# Visualización de las distribuciones
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.hist(datos_normal, bins=30, color='skyblue', edgecolor='black')
ax1.set_title('Distribución Normal')
ax1.set_xlabel('Valor')
ax1.set_ylabel('Frecuencia')

ax2.hist(datos_binomial, bins=30, color='salmon', edgecolor='black')
ax2.set_title('Distribución Binomial')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()
