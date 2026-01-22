
class State:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def __repr__(self):
        return f"State({self.value})"

class StateSpace:
    def __init__(self):
        self.states = []

    def add_state(self, value, parent=None):
        new_state = State(value, parent)
        self.states.append(new_state)

    def show_states(self):
        for state in self.states:
            print(f"Estado: {state.value}, Padre: {state.parent.value if state.parent else None}")

# Crear un espacio de estados
state_space = StateSpace()
state_space.add_state("Inicio")
state_space.add_state("Estado 1", "Inicio")
state_space.add_state("Estado 2", "Inicio")
state_space.add_state("Estado 3", "Estado 1")

# Mostrar los estados
state_space.show_states()
