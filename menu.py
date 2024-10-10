class Plato:
    def __init__(self, nombre, precio, descripcion=""):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}\nDescripción: {self.descripcion}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def mostrar_categoria(self):
        print(f"\n{self.nombre}")
        print("-" * len(self.nombre))
        for plato in self.platos:
            print(plato)

class Menu:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_menu(self):
        for categoria in self.categorias:
            categoria.mostrar_categoria()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear platos
    plato1 = Plato("Ensalada César", 8.50, "Ensalada con lechuga romana, crotones, y aderezo César.")
    plato2 = Plato("Sopa de Tomate", 6.00, "Sopa de tomate fresca con albahaca.")
    plato3 = Plato("Pizza Margarita", 12.00, "Pizza clásica con tomate, mozzarella y albahaca fresca.")
    
    # Crear categorías
    ensaladas = Categoria("Ensaladas")
    sopas = Categoria("Sopas")
    pizzas = Categoria("Pizzas")
    
    # Agregar platos a categorías
    ensaladas.agregar_plato(plato1)
    sopas.agregar_plato(plato2)
    pizzas.agregar_plato(plato3)
    
    # Crear menú
    menu = Menu()
    menu.agregar_categoria(ensaladas)
    menu.agregar_categoria(sopas)
    menu.agregar_categoria(pizzas)
    
    # Mostrar mi menú
    menu.mostrar_menu()
