
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la semilla para reproducibilidad
np.random.seed(0)

# Generación de datos con incertidumbre (distribución normal)
media = 50
desviacion_estandar = 10
datos = np.random.normal(media, desviacion_estandar, 1000)

# Visualización de la incertidumbre con histograma
plt.hist(datos, bins=30, edgecolor='black', alpha=0.7)
plt.title("Distribución de Incertidumbre (Normal)")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Medidas de incertidumbre
print("Media de los datos:", np.mean(datos))
print("Desviación estándar de los datos:", np.std(datos))
print("Varianza de los datos:", np.var(datos))
