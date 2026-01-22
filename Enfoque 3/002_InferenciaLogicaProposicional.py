
# Función para comprobar si una proposición es verdadera
def is_true(clauses, interpretation):
    for clause in clauses:
        if not any(literal if literal > 0 else not interpretation[-literal] for literal in clause):
            return False
    return True

# Función para realizar la inferencia
def propositional_inference(clauses, interpretation):
    if is_true(clauses, interpretation):
        return True
    
    # Buscar resolventes
    for clause in clauses:
        for literal in clause:
            new_interpretation = interpretation.copy()
            new_interpretation[abs(literal)] = literal > 0
            
            if propositional_inference(clauses, new_interpretation):
                return True
    return False

# Ejemplo de uso
# Claúsulas: P o Q, no P o R
clauses = [
    [1, 2],  # P v Q
    [-1, 3]  # ¬P v R
]

# Probar una interpretación (P=Verdadero, Q=Falso, R=Falso)
interpretation = [False, True, False, False]  # P=1, Q=2, R=3

result = propositional_inference(clauses, interpretation)
print("La inferencia es:", result)
