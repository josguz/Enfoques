
class Ontology:
    def __init__(self):
        self.classes = {}
    
    def add_class(self, class_name, parent_class=None):
        self.classes[class_name] = {"parent": parent_class, "instances": []}

    def add_instance(self, class_name, instance_name):
        if class_name in self.classes:
            self.classes[class_name]["instances"].append(instance_name)
        else:
            print(f"La clase '{class_name}' no existe.")

    def show_ontology(self):
        for class_name, info in self.classes.items():
            print(f"Clase: {class_name}, Padre: {info['parent']}, Instancias: {info['instances']}")

# Crear una ontología
ontology = Ontology()
ontology.add_class("Animal")
ontology.add_class("Mamífero", "Animal")
ontology.add_class("Pájaro", "Animal")
ontology.add_instance("Mamífero", "Perro")
ontology.add_instance("Mamífero", "Gato")
ontology.add_instance("Pájaro", "Loro")

# Mostrar la ontología
ontology.show_ontology()
