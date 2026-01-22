
class Taxonomy:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name, parent_category=None):
        self.categories[category_name] = {"parent": parent_category, "objects": []}

    def add_object(self, category_name, object_name):
        if category_name in self.categories:
            self.categories[category_name]["objects"].append(object_name)
        else:
            print(f"La categoría '{category_name}' no existe.")

    def show_taxonomy(self):
        for category_name, info in self.categories.items():
            print(f"Categoría: {category_name}, Padre: {info['parent']}, Objetos: {info['objects']}")

# Crear una taxonomía
taxonomy = Taxonomy()
taxonomy.add_category("Animal")
taxonomy.add_category("Mamífero", "Animal")
taxonomy.add_category("Ave", "Animal")
taxonomy.add_object("Mamífero", "Perro")
taxonomy.add_object("Mamífero", "Gato")
taxonomy.add_object("Ave", "Loro")

# Mostrar la taxonomía
taxonomy.show_taxonomy()
