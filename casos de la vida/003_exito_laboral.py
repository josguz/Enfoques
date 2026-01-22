# El resto del código permanece igual
import numpy as np

# Modelo probabilista para predecir éxito en una entrevista de trabajo
class EntrevistaModeloProbabilista:
    def __init__(self):
        self.factores = {}
    
    def agregar_factor(self, factor, probabilidad):
        """Agrega un factor con su probabilidad de influir en el éxito de la entrevista"""
        self.factores[factor] = probabilidad
    
    def calcular_exito(self):
        """Calcula la probabilidad de éxito en la entrevista con base en los factores registrados"""
        if not self.factores:
            return "No hay factores registrados."
        
        # Se asume que los factores son independientes y se combinan de forma multiplicativa
        probabilidad_exito = np.prod(list(self.factores.values()))
        return f"Probabilidad de éxito en la entrevista: {probabilidad_exito * 100:.2f}%"

# Crear el modelo de entrevista
modelo = EntrevistaModeloProbabilista()

# Agregar factores y sus probabilidades estimadas
modelo.agregar_factor("Experiencia relevante", 0.85)
modelo.agregar_factor("Habilidades técnicas", 0.75)
modelo.agregar_factor("Comunicación efectiva", 0.80)
modelo.agregar_factor("Confianza en la entrevista", 0.70)
modelo.agregar_factor("Conocimiento de la empresa", 0.65)

# Calcular y mostrar la probabilidad de éxito
total_exito = modelo.calcular_exito()
print(total_exito)