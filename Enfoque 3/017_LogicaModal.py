
# Ejemplo de lógica modal
class ModalLogic:
    def __init__(self):
        self.knowledge_base = {}

    def add_fact(self, proposition, is_possible=True):
        self.knowledge_base[proposition] = is_possible

    def is_possible(self, proposition):
        return self.knowledge_base.get(proposition, False)

# Crear un sistema de lógica modal
modal_logic = ModalLogic()
modal_logic.add_fact("Es posible que llueva", True)
modal_logic.add_fact("Es necesario que estudies", False)

# Consultar proposiciones modales
print("¿Es posible que llueva?", modal_logic.is_possible("Es posible que llueva"))
print("¿Es necesario que estudies?", modal_logic.is_possible("Es necesario que estudies"))
