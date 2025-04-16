# sistema_empleados.py

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: ${self.salario}")

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado a {self.nombre}.")

    def listar_empleados(self):
        print(f"Lista de empleados en {self.nombre}:")
        for emp in self.empleados:
            emp.mostrar_info()

    def calcular_gastos_mensuales(self):
        total = sum(emp.salario for emp in self.empleados)
        print(f"Gastos mensuales en salarios: ${total}")

# Ejemplo de uso
if __name__ == "__main__":
    empresa = Empresa("MiEmpresa S.A.")
    empresa.agregar_empleado(Empleado("Ana", "Contadora", 50000))
    empresa.agregar_empleado(Empleado("Luis", "DevOps", 60000))
    empresa.listar_empleados()
    empresa.calcular_gastos_mensuales()


https://chatgpt.com/share/68001622-a9a8-8004-84c6-a8c64181dc7f