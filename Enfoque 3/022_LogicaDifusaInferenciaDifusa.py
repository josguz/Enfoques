
class FuzzyInferenceSystem:
    def __init__(self):
        self.rules = []
    
    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))
    
    def infer(self, input_value):
        output = 0
        for condition, conclusion in self.rules:
            membership = condition(input_value)
            output += membership * conclusion(input_value)
        return output

# Funciones de membresía para condiciones
def low_temperature(temp):
    return max(0, min(1, (20 - temp) / 10))  # Bajo

def high_temperature(temp):
    return max(0, min(1, (temp - 30) / 10))  # Alto

# Funciones de conclusión
def fan_speed(temp):
    if low_temperature(temp):
        return 0  # Apagar ventilador
    elif high_temperature(temp):
        return 100  # Ventilador al máximo
    return 50  # Velocidad media

# Crear el sistema de inferencia difusa
fis = FuzzyInferenceSystem()
fis.add_rule(low_temperature, fan_speed)
fis.add_rule(high_temperature, fan_speed)

# Inferir velocidad del ventilador para una temperatura dada
input_temperature = 25
output_speed = fis.infer(input_temperature)
print(f"Temperatura: {input_temperature}°C - Velocidad del ventilador: {output_speed}")
