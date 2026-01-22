
class LogicalAgent:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def decide_action(self, condition):
        if condition in self.knowledge_base:
            return self.knowledge_base[condition]
        else:
            return "No se puede tomar una decisión."

# Base de conocimiento del agente
knowledge_base = {
    "Hace calor": "Enciende el ventilador",
    "Está lloviendo": "Cierra la ventana",
    "Es de noche": "Enciende la luz"
}

# Crear el agente lógico
agent = LogicalAgent(knowledge_base)

# Decidir acción basada en una condición
condition = "Hace calor"
action = agent.decide_action(condition)
print(f"Condición: {condition} - Acción: {action}")
