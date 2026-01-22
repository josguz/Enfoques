
class Agent:
    def __init__(self, name):
        self.name = name

    def act(self, action):
        print(f"{self.name} está realizando la acción: {action}")

class ContinuousPlanner:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def execute_plan(self):
        for agent in self.agents:
            # Simulación de acciones de los agentes
            action = "Recoger un objeto"
            agent.act(action)

# Crear agentes
agent1 = Agent("Agente 1")
agent2 = Agent("Agente 2")

# Crear un planificador continuo y agregar agentes
planner = ContinuousPlanner()
planner.add_agent(agent1)
planner.add_agent(agent2)

# Ejecutar el plan
planner.execute_plan()
