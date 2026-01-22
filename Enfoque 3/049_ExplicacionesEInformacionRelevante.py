
class ExplanationSystem:
    def __init__(self):
        self.knowledge_base = {}

    def add_fact(self, fact, explanation):
        self.knowledge_base[fact] = explanation

    def explain(self, fact):
        return self.knowledge_base.get(fact, "No hay explicación disponible.")

# Crear un sistema de explicaciones
explanation_system = ExplanationSystem()
explanation_system.add_fact("El agua hierve a 100 grados Celsius", "Esto ocurre debido a la presión atmosférica.")
explanation_system.add_fact("Los objetos caen debido a la gravedad", "La gravedad es una fuerza que atrae los objetos hacia el centro de la Tierra.")

# Obtener explicaciones
fact_to_explain = "El agua hierve a 100 grados Celsius"
print(f"Explicación para '{fact_to_explain}':", explanation_system.explain(fact_to_explain))

fact_to_explain = "Los objetos caen debido a la gravedad"
print(f"Explicación para '{fact_to_explain}':", explanation_system.explain(fact_to_explain))

fact_to_explain = "La luna está hecha de queso"
print(f"Explicación para '{fact_to_explain}':", explanation_system.explain(fact_to_explain))  # Sin explicación
