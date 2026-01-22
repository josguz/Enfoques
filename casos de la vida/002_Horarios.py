import itertools

# Función para verificar si una asignación cumple con las restricciones
def cumple_restricciones(asignacion, profesores):
    horarios_ocupados = {}  # Diccionario para rastrear qué aulas están ocupadas en cada horario
    profesores_ocupados = {}  # Diccionario para rastrear qué profesores están ocupados en cada horario

    for materia, (horario, aula) in asignacion.items():
        profesor = profesores[materia]

        # Verificar que el aula no esté ocupada en el mismo horario
        if horario in horarios_ocupados and horarios_ocupados[horario] == aula:
            return False
        horarios_ocupados[horario] = aula

        # Verificar que el profesor no tenga dos clases al mismo tiempo
        if horario in profesores_ocupados and profesores_ocupados[horario] == profesor:
            return False
        profesores_ocupados[horario] = profesor

    return True

# Algoritmo de vuelta atrás para encontrar una asignación válida de horarios
def asignar_horarios(materias, horarios, aulas, profesores):
    # Definir dominios posibles para cada materia (combinaciones de horarios y aulas disponibles)
    dominios = {materia: list(itertools.product(horarios, aulas)) for materia in materias}
    
    # Función recursiva de backtracking para asignar horarios
    def backtracking(asignacion={}):
        # Si todas las materias tienen horario asignado, se ha encontrado una solución válida
        if len(asignacion) == len(materias):
            return asignacion  # Solución encontrada

        # Seleccionar la siguiente materia sin asignación
        materia = [m for m in materias if m not in asignacion][0]

        # Probar cada combinación posible de horario y aula para la materia seleccionada
        for horario_aula in dominios[materia]:
            asignacion[materia] = horario_aula
            # Si la asignación actual cumple con las restricciones, continuar con la siguiente materia
            if cumple_restricciones(asignacion, profesores):
                resultado = backtracking(asignacion)
                if resultado:
                    return resultado  # Retornar la solución si se encuentra
            asignacion.pop(materia)  # Deshacer asignación si no funciona

        return None  # No se encontró solución válida

    return backtracking()

# Datos de entrada: materias, profesores, horarios y aulas disponibles
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Programación']
profesores = {
    'Matemáticas': 'Prof. A',
    'Física': 'Prof. B',
    'Química': 'Prof. C',
    'Historia': 'Prof. D',
    'Programación': 'Prof. E'
}
horarios = ['Lunes 8-10', 'Lunes 10-12', 'Martes 8-10', 'Martes 10-12', 
            'Miércoles 8-10', 'Miércoles 10-12', 'Jueves 8-10', 'Jueves 10-12']
aulas = ['Aula 101', 'Aula 102', 'Aula 103']

# Ejecutar la asignación de horarios
solucion = asignar_horarios(materias, horarios, aulas, profesores)

# Mostrar resultado
if solucion:
    print("Horario de clases asignado:")
    for materia, (horario, aula) in solucion.items():
        print(f"{materia}: {horario}, {aula}")
else:
    print("No se encontró una solución válida.")