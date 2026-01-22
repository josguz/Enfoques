
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo (una serie de tiempo con tendencia y ruido)
np.random.seed(0)
datos = np.linspace(10, 30, 100) + np.random.normal(0, 2, 100)

# Filtrado (media móvil para reducir ruido)
def filtrado(serie, ventana=5):
    return np.convolve(serie, np.ones(ventana) / ventana, mode='valid')

# Predicción (predecir el próximo valor usando la tendencia de los últimos puntos)
def prediccion(serie, puntos=5):
    return np.mean(serie[-puntos:])

# Suavizado (media exponencial para reducir variabilidad)
def suavizado(serie, alpha=0.3):
    suavizada = [serie[0]]
    for valor in serie[1:]:
        suavizada.append(alpha * valor + (1 - alpha) * suavizada[-1])
    return suavizada

# Visualización de los resultados
filtrada = filtrado(datos)
suavizada = suavizado(datos)
prediccion_valor = prediccion(datos)

plt.plot(datos, label="Datos originales")
plt.plot(range(len(filtrada)), filtrada, label="Filtrado (Media móvil)")
plt.plot(suavizada, label="Suavizado (Media exponencial)")
plt.axhline(prediccion_valor, color='red', linestyle='--', label=f"Predicción próxima: {prediccion_valor:.2f}")
plt.legend()
plt.title("Filtrado, Predicción y Suavizado de Serie de Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()
