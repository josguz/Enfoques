
# Ejemplo de lógica temporal
class TemporalLogic:
    def __init__(self):
        self.time_points = {}

    def add_fact(self, time, proposition):
        self.time_points[time] = proposition

    def evaluate(self, time):
        return self.time_points.get(time, "No hay información en este momento.")

# Crear un sistema de lógica temporal
temporal_logic = TemporalLogic()
temporal_logic.add_fact("t1", "El sistema está encendido.")
temporal_logic.add_fact("t2", "El sistema está apagado.")

# Consultar proposiciones temporales
print("Estado en t1:", temporal_logic.evaluate("t1"))
print("Estado en t2:", temporal_logic.evaluate("t2"))
print("Estado en t3:", temporal_logic.evaluate("t3"))  # Sin información
