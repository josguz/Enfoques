
class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def show_task(self, level=0):
        indent = "  " * level
        print(f"{indent}Tarea: {self.name}")
        for subtask in self.subtasks:
            subtask.show_task(level + 1)

# Crear tareas y subtareas
main_task = Task("Preparar la cena")
subtask1 = Task("Cocinar el pollo")
subtask2 = Task("Hacer ensalada")
subtask3 = Task("Poner la mesa")

main_task.add_subtask(subtask1)
main_task.add_subtask(subtask2)
main_task.add_subtask(subtask3)

# Mostrar la red jerárquica de tareas
main_task.show_task()
