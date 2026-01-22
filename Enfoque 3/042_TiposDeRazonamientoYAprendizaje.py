
class Reasoning:
    def deductive(self, premises):
        print("Razonamiento deductivo:")
        conclusion = all(premises)  # Conclusión basada en premisas
        print("Conclusión:", conclusion)

    def inductive(self, observations):
        print("Razonamiento inductivo:")
        conclusion = any(observations)  # Conclusión basada en observaciones
        print("Conclusión:", conclusion)

class Learning:
    def supervised(self, data):
        print("Aprendizaje supervisado:")
        model = "Modelo entrenado con datos etiquetados"
        print(model)

    def unsupervised(self, data):
        print("Aprendizaje no supervisado:")
        clusters = "Datos agrupados en clusters"
        print(clusters)

# Crear instancias de razonamiento y aprendizaje
reasoning = Reasoning()
learning = Learning()

# Razonamiento
reasoning.deductive([True, True])  # Premisas verdaderas
reasoning.inductive([True, False])  # Observaciones

# Aprendizaje
learning.supervised([("dato1", "etiqueta1"), ("dato2", "etiqueta2")])
learning.unsupervised([("dato1",), ("dato2",), ("dato3",)])
