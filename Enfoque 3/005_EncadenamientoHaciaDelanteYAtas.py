
# Ejemplo de encadenamiento hacia adelante
def forward_chaining(knowledge_base, query):
    inferred = set()
    while True:
        new_inferences = set()
        for premise, conclusion in knowledge_base:
            if premise.issubset(inferred) and conclusion not in inferred:
                new_inferences.add(conclusion)
        if not new_inferences:
            break
        inferred.update(new_inferences)
    return query in inferred

# Ejemplo de encadenamiento hacia atrás
def backward_chaining(knowledge_base, query):
    for premise, conclusion in knowledge_base:
        if conclusion == query:
            if premise.issubset(inferred) or backward_chaining(knowledge_base, premise):
                return True
    return False

# Base de conocimiento
knowledge_base = {
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"E"}, "F")
}

# Inferir usando encadenamiento hacia adelante
inferred = set()
query = "D"
is_provable_forward = forward_chaining(knowledge_base, query)
print(f"Encadenamiento hacia adelante: ¿Se puede inferir '{query}'? {is_provable_forward}")

# Inferir usando encadenamiento hacia atrás
query = "C"
is_provable_backward = backward_chaining(knowledge_base, query)
print(f"Encadenamiento hacia atrás: ¿Se puede inferir '{query}'? {is_provable_backward}")
