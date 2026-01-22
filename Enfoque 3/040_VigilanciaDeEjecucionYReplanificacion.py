
class ExecutionMonitor:
    def __init__(self):
        self.plans = []
        self.execution_status = {}

    def add_plan(self, plan):
        self.plans.append(plan)
        self.execution_status[plan] = False  # Estado inicial: no ejecutado

    def execute_plans(self):
        for plan in self.plans:
            print(f"Ejecutando plan: {plan}")
            self.execution_status[plan] = True  # Marcar como ejecutado
            # Simulación de cambio en la ejecución
            if plan == "Plan de emergencia":
                print("Replanificando...")
                self.replan(plan)

    def replan(self, failed_plan):
        print(f"Replanificando {failed_plan}...")
        # Lógica de replanteamiento
        new_plan = "Nuevo plan basado en condiciones actuales"
        self.add_plan(new_plan)

# Crear un monitor de ejecución
monitor = ExecutionMonitor()
monitor.add_plan("Plan de rutina")
monitor.add_plan("Plan de emergencia")

# Ejecutar planes
monitor.execute_plans()
