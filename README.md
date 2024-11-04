# sistema-compras-ropas
 
Este proyecto es un sistema de compras de ropa desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite a los usuarios seleccionar productos de ropa, agregarlos a un carrito y realizar compras.

## Estructura del Proyecto

- **tienda_ropa.py**: Contiene la implementación del sistema de compras de ropa.
  
## Clases Implementadas

- **Producto**: Clase base que representa un producto general.
- **Ropa**: Clase que hereda de Producto y añade características específicas de la ropa.
- **Camisa**: Clase que representa camisas y hereda de Ropa.
- **Pantalon**: Clase que representa pantalones y hereda de Ropa.
- **Zapato**: Clase que representa zapatos y hereda de Ropa.
- **Carrito**: Clase que maneja los productos seleccionados para la compra.
- **Tienda**: Clase que maneja los productos disponibles y las compras.

## Pilares de POO Aplicados

1. **Encapsulamiento**: Los atributos de las clases están encapsulados y se accede a ellos mediante métodos getters.
2. **Herencia**: Las clases **Camisa**, **Pantalon**, y **Zapato** heredan de **Ropa**, que a su vez hereda de **Producto**.
3. **Polimorfismo**: Cada clase hija sobrescribe el método `mostrar_info` para mostrar información específica del producto.
4. **Abstracción**: La lógica interna del sistema está oculta al usuario, que solo interactúa con el menú de selección de productos y el proceso de compra.

## Uso

1. Clona este repositorio en tu máquina local.
2. Ejecuta el archivo `tienda_ropa.py` usando Python.
3. Sigue las instrucciones en pantalla para seleccionar productos y realizar una compra.

## Ejemplo de Ejecución

Al ejecutar el programa, se mostrarán los productos disponibles y podrás seleccionarlos para agregarlos al carrito. Al finalizar la compra, se mostrará un resumen de los productos seleccionados y el total a pagar.

## Requisitos

- Python 3.x