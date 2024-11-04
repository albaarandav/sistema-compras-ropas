class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio  # Atributo encapsulado

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: ${self._precio:.2f}")


class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla  # Atributo encapsulado

    @property
    def talla(self):
        return self._talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela  # Atributo encapsulado

    @property
    def tipo_tela(self):
        return self._tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Tela: {self._tipo_tela}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_corte):
        super().__init__(nombre, precio, talla)
        self._tipo_corte = tipo_corte  # Atributo encapsulado

    @property
    def tipo_corte(self):
        return self._tipo_corte

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Corte: {self._tipo_corte}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla)
        self._tipo_material = tipo_material  # Atributo encapsulado

    @property
    def tipo_material(self):
        return self._tipo_material

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Material: {self._tipo_material}")


class Carrito:
    def __init__(self):
        self._productos = []  # Atributo privado

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = sum(producto.precio for producto in self._productos)
        return total

    def mostrar_carrito(self):
        if not self._productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self._productos:
                producto.mostrar_info()
            print(f"Total a pagar: ${self.calcular_total():.2f}")


class Tienda:
    def __init__(self):
        self._productos_disponibles = []

    def agregar_producto(self, producto):
        self._productos_disponibles.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for i, producto in enumerate(self._productos_disponibles):
            print(f"{i + 1}. ", end="")
            producto.mostrar_info()

    def comprar(self):
        carrito = Carrito()
        while True:
            self.mostrar_productos()
            seleccion = input("Seleccione un producto (número) o 'salir' para finalizar: ")
            if seleccion.lower() == 'salir':
                break
            try:
                index = int(seleccion) - 1
                if 0 <= index < len(self._productos_disponibles):
                    carrito.agregar_producto(self._productos_disponibles[index])
                    print(f"{self._productos_disponibles[index].nombre} ha sido añadido al carrito.")
                else:
                    print("Selección no válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        carrito.mostrar_carrito()


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()

    # Agregar productos a la tienda
    camisa1 = Camisa("Camisa de Hombre", 25.00, "M", "Algodón")
    pantalon1 = Pantalon("Pantalón de Hombre", 30.00, "L", "Slim")
    zapato1 = Zapato("Zapatos de Hombre", 60.00, "42", "Cuero")

    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapato1)

    # Iniciar el proceso de compra
    tienda.comprar()
