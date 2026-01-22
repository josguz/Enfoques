
# Simulación de un entorno Prolog simple
class PrologEnvironment:
    def __init__(self):
        self.facts = {}
    
    def add_fact(self, key, value):
        self.facts[key] = value

    def query(self, key):
        return self.facts.get(key, None)

# Crear un entorno Prolog
prolog_env = PrologEnvironment()
prolog_env.add_fact("padre(Juan, Maria)", True)
prolog_env.add_fact("padre(Juan, Pedro)", True)
prolog_env.add_fact("madre(Maria, Ana)", True)

# Realizar consultas
print("Consulta: ¿Juan es padre de Maria?", prolog_env.query("padre(Juan, Maria)"))
print("Consulta: ¿Juan es padre de Ana?", prolog_env.query("padre(Juan, Ana)"))
