
class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_relation(self, subject, relation, object_):
        if subject not in self.network:
            self.network[subject] = {}
        self.network[subject][relation] = object_

    def show_network(self):
        for subject, relations in self.network.items():
            for relation, object_ in relations.items():
                print(f"{subject} --[{relation}]--> {object_}")

# Crear una red semántica
semantic_network = SemanticNetwork()
semantic_network.add_relation("Perro", "es un", "Animal")
semantic_network.add_relation("Gato", "es un", "Animal")
semantic_network.add_relation("Animal", "tiene", "Vida")

# Mostrar la red semántica
semantic_network.show_network()
