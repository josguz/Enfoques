
class GraphPlan:
    def __init__(self):
        self.actions = []
        self.goals = []
        self.plan = []

    def add_action(self, action):
        self.actions.append(action)

    def set_goals(self, goals):
        self.goals = goals

    def generate_plan(self):
        # Simulación de la generación de un plan (simplificado)
        for goal in self.goals:
            if goal in self.actions:
                self.plan.append(goal)

    def show_plan(self):
        print("Plan generado:")
        for action in self.plan:
            print(f" - {action}")

# Crear un sistema de planificación
graph_plan = GraphPlan()
graph_plan.add_action("Recoger el objeto")
graph_plan.add_action("Llevar el objeto a la mesa")
graph_plan.set_goals(["Recoger el objeto", "Llevar el objeto a la mesa"])

# Generar y mostrar el plan
graph_plan.generate_plan()
graph_plan.show_plan()
