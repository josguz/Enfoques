
class PartialPlan:
    def __init__(self):
        self.actions = []
        self.order_constraints = []

    def add_action(self, action):
        self.actions.append(action)

    def add_order_constraint(self, before_action, after_action):
        self.order_constraints.append((before_action, after_action))

    def show_plan(self):
        print("Plan de Acción:")
        for action in self.actions:
            print(f" - {action}")

        print("Restricciones de Orden:")
        for before, after in self.order_constraints:
            print(f" - {before} antes de {after}")

# Crear un plan parcial
partial_plan = PartialPlan()
partial_plan.add_action("Recoger el objeto")
partial_plan.add_action("Llevar el objeto a la mesa")
partial_plan.add_order_constraint("Recoger el objeto", "Llevar el objeto a la mesa")

# Mostrar el plan parcial
partial_plan.show_plan()
