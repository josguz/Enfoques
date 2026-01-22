
from itertools import product

class SATPlan:
    def __init__(self):
        self.actions = []
        self.state = {}

    def add_action(self, action, preconditions, effects):
        self.actions.append({"action": action, "preconditions": preconditions, "effects": effects})

    def plan(self, initial_state, goal_state):
        self.state = initial_state
        for action in self.actions:
            if all(self.state.get(cond, False) for cond in action["preconditions"]):
                print(f"Ejecutando acción: {action['action']}")
                for effect in action["effects"]:
                    self.state[effect] = True  # Aplicar efectos

        return all(self.state.get(goal, False) for goal in goal_state)

# Crear un planificador SATPLAN
sat_plan = SATPlan()
sat_plan.add_action("Recoger objeto", ["Objeto en el suelo"], ["Objeto recogido"])
sat_plan.add_action("Llevar objeto", ["Objeto recogido"], ["Objeto en la mesa"])

# Estado inicial y objetivo
initial_state = {"Objeto en el suelo": True, "Objeto recogido": False}
goal_state = ["Objeto en la mesa"]

# Planificar
if sat_plan.plan(initial_state, goal_state):
    print("Planificación exitosa. Objetivos alcanzados.")
else:
    print("No se pudo alcanzar el objetivo.")
