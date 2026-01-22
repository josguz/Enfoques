
class VersionSpace:
    def __init__(self):
        self.versions = []

    def add_version(self, version):
        self.versions.append(version)

    def find_most_specific(self):
        # Simulación de búsqueda de la versión más específica
        if not self.versions:
            return None
        return min(self.versions, key=len)  # La versión más específica es la de menor longitud

# Crear un espacio de versiones
version_space = VersionSpace()
version_space.add_version("Sujeto: A, Predicado: B")
version_space.add_version("Sujeto: A")
version_space.add_version("Sujeto: A, Predicado: C")

# Encontrar la versión más específica
most_specific = version_space.find_most_specific()
print("La versión más específica es:", most_specific)
