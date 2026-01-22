
# Definición de un conjunto de eventos
eventos = ['sol', 'lluvia', 'nieve', 'sol', 'sol', 'nieve', 'lluvia', 'sol', 'nieve', 'sol', 'lluvia']


# Cálculo de la probabilidad a priori de cada evento
def probabilidad_a_priori(eventos):
    total_eventos = len(eventos)
    probabilidad_eventos = {evento: eventos.count(evento) / total_eventos for evento in set(eventos)}
    return probabilidad_eventos

# Ejemplo de uso
probabilidades = probabilidad_a_priori(eventos)
print("Probabilidades a Priori:", probabilidades)
