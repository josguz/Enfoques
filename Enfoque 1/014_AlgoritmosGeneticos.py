
import random

# Parámetros del algoritmo genético
tamano_poblacion = 6
generaciones = 10
tasa_mutacion = 0.1

# Función objetivo para maximizar (aquí intentamos maximizar la suma de los genes)
def aptitud(individuo):
    return sum(individuo)

# Crear una población inicial aleatoria
def crear_poblacion(tamano):
    return [[random.randint(0, 1) for _ in range(5)] for _ in range(tamano)]

# Selección por torneo
def seleccion(poblacion):
    padre1 = max(random.sample(poblacion, 2), key=aptitud)
    padre2 = max(random.sample(poblacion, 2), key=aptitud)
    return padre1, padre2

# Cruza dos padres para producir dos hijos
def cruza(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

# Realiza una mutación en un hijo con cierta probabilidad
def mutacion(individuo, tasa_mutacion):
    return [gen if random.random() > tasa_mutacion else 1 - gen for gen in individuo]

# Algoritmo genético
def algoritmo_genetico():
    poblacion = crear_poblacion(tamano_poblacion)
    for generacion in range(generaciones):
        print(f"Generación {generacion + 1}:")
        poblacion = sorted(poblacion, key=aptitud, reverse=True)
        print("Mejor individuo:", poblacion[0], "Aptitud:", aptitud(poblacion[0]))

        nueva_poblacion = poblacion[:2]  # Elitismo: los 2 mejores pasan directamente
        while len(nueva_poblacion) < tamano_poblacion:
            padre1, padre2 = seleccion(poblacion)
            hijo1, hijo2 = cruza(padre1, padre2)
            nueva_poblacion.extend([mutacion(hijo1, tasa_mutacion), mutacion(hijo2, tasa_mutacion)])
        
        poblacion = nueva_poblacion

# Ejecutar el algoritmo genético
algoritmo_genetico()
