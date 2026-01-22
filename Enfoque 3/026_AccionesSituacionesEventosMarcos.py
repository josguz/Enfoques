
class Frame:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.events = []

    def add_attribute(self, attribute, value):
        self.attributes[attribute] = value

    def add_event(self, event):
        self.events.append(event)

    def show_frame(self):
        print(f"Marco: {self.name}")
        print("Atributos:", self.attributes)
        print("Eventos:", self.events)

# Crear un marco para una situación
situation_frame = Frame("Fiesta")
situation_frame.add_attribute("Lugar", "Casa de Juan")
situation_frame.add_attribute("Hora", "18:00")
situation_frame.add_event("Llegan los invitados")
situation_frame.add_event("Se sirve la comida")

# Mostrar el marco
situation_frame.show_frame()
