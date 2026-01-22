
import numpy as np
import matplotlib.pyplot as plt

# Generar una serie de tiempo estacionaria (ruido blanco)
np.random.seed(0)
serie_estacionaria = np.random.normal(loc=0, scale=1, size=100)

# Función para calcular la media y varianza en distintos segmentos
def verificar_estacionariedad(serie, segmentos=5):
    tamaño_segmento = len(serie) // segmentos
    medias = []
    varianzas = []
    
    for i in range(segmentos):
        segmento = serie[i * tamaño_segmento: (i + 1) * tamaño_segmento]
        medias.append(np.mean(segmento))
        varianzas.append(np.var(segmento))
    
    return medias, varianzas

# Visualización de la serie de tiempo
plt.plot(serie_estacionaria)
plt.title("Serie de Tiempo Estacionaria (Ruido Blanco)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()

# Ejemplo de uso
medias, varianzas = verificar_estacionariedad(serie_estacionaria)
print("Medias de segmentos:", medias)
print("Varianzas de segmentos:", varianzas)
