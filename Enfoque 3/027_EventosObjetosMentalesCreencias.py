
class MentalEvent:
    def __init__(self, name):
        self.name = name
        self.beliefs = {}

    def add_belief(self, belief, truth_value):
        self.beliefs[belief] = truth_value

    def show_event(self):
        print(f"Evento Mental: {self.name}")
        for belief, truth_value in self.beliefs.items():
            print(f"  Creencia: '{belief}' - Verdadero: {truth_value}")

# Crear un evento mental
event = MentalEvent("Cumpleaños de Juan")
event.add_belief("Juan tiene 30 años", True)
event.add_belief("Hoy es su cumpleaños", True)
event.add_belief("Juan no se siente feliz", False)

# Mostrar el evento y sus creencias
event.show_event()
