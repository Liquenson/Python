# task.py - Módulo que representa una tarea
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.title}: {self.description}"


# task_manager.py - Módulo que maneja la lógica de las tareas
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarea '{task.title}' añadida.")

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        print(f"Tarea '{title}' eliminada.")

    def show_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        else:
            for task in self.tasks:
                print(task)


# main.py - Módulo principal que ejecuta el programa
def main():
    manager = TaskManager()

    while True:
        print("\n1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            title = input("Título de la tarea: ")
            description = input("Descripción de la tarea: ")
            task = Task(title, description)
            manager.add_task(task)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            title = input("Título de la tarea a eliminar: ")
            manager.remove_task(title)

        elif choice == "4":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()