
class STRIPSPlanner:
    def __init__(self):
        self.actions = []

    def add_action(self, name, preconditions, effects):
        self.actions.append({"name": name, "preconditions": preconditions, "effects": effects})

    def plan(self, state):
        plan = []
        for action in self.actions:
            if all(state.get(precondition, False) for precondition in action["preconditions"]):
                plan.append(action["name"])
                for effect in action["effects"]:
                    state[effect] = True  # Aplicar efectos
        return plan, state

# Crear un planificador STRIPS
planner = STRIPSPlanner()
planner.add_action("Recoger objeto", ["Objeto en el suelo"], ["Objeto recogido"])
planner.add_action("Colocar objeto", ["Objeto recogido"], ["Objeto en la mesa"])

# Estado inicial
initial_state = {"Objeto en el suelo": True, "Objeto recogido": False}

# Planificar acciones
plan, final_state = planner.plan(initial_state)
print("Plan de acción:", plan)
print("Estado final:", final_state)
