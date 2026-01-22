
class ConditionalPlan:
    def __init__(self):
        self.actions = []
        self.conditions = {}

    def add_action(self, action, condition):
        self.actions.append(action)
        self.conditions[action] = condition

    def execute(self):
        for action in self.actions:
            if self.conditions[action]():
                print(f"Ejecutando acción: {action}")

# Crear un plan condicional
conditional_plan = ConditionalPlan()

# Definir acciones y condiciones
def check_condition_1():
    return True  # Siempre verdadera

def check_condition_2():
    return False  # Siempre falsa

conditional_plan.add_action("Recoger el objeto", check_condition_1)
conditional_plan.add_action("Llevar el objeto a la mesa", check_condition_2)

# Ejecutar el plan condicional
conditional_plan.execute()
