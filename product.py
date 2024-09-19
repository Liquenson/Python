# product.py - Módulo que representa un producto
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"Producto: {self.name}, Cantidad: {self.quantity}, Precio: ${self.price:.2f}"


# inventory_manager.py - Módulo que maneja la lógica del inventario
class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.name in self.inventory:
            self.inventory[product.name].update_quantity(product.quantity)
        else:
            self.inventory[product.name] = product
        print(f"Producto '{product.name}' añadido/actualizado.")

    def remove_product(self, product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
            print(f"Producto '{product_name}' eliminado.")
        else:
            print(f"Producto '{product_name}' no encontrado.")

    def show_inventory(self):
        if not self.inventory:
            print("No hay productos en el inventario.")
        else:
            for product in self.inventory.values():
                print(product)


# main.py - Módulo principal que ejecuta el programa
def main():
    manager = InventoryManager()

    while True:
        print("\n1. Añadir producto")
        print("2. Ver inventario")
        print("3. Eliminar producto")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            product = Product(name, quantity, price)
            manager.add_product(product)

        elif choice == "2":
            manager.show_inventory()

        elif choice == "3":
            product_name = input("Nombre del producto a eliminar: ")
            manager.remove_product(product_name)

        elif choice == "4":
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()