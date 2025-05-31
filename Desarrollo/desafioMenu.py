inventario = {"Comics": 10, "Libros": 15, "Mangas": 3}
def agregarProducto (producto, stock):
    inventario[producto] = stock;
def mostrarInventario():
    return inventario;
def eliminarProducto(producto):
    inventario.pop(producto);
def buscarProducto(producto):
    return f"El stock de '{str(producto)}' es {inventario[producto]}";

while True:
    print("------------------------------")
    print("A. Agregar producto | B. Mostrar inventario | C. Eliminar producto | D. Buscar Producto | E. Salir")
    print("------------------------------")
    
    opcionMenu = input("> ").upper()
    
    if opcionMenu == "A":
        nuevoProducto = input("Elegir nombre del nuevo producto ---> ");
        nuevoStock = input("Introducir stock del nuevo producto ---> ");
        agregarProducto(nuevoProducto, nuevoStock);
    elif opcionMenu == "B":
        print(mostrarInventario());
    elif opcionMenu == "C":
        productoEliminado = input("Introducir clave del producto a eliminar ---> ");
        eliminarProducto(productoEliminado);
    elif opcionMenu == "D":
        productoBuscado = input("Introducir clave del producto a buscar ---> ");
        print(buscarProducto(productoBuscado));
    elif opcionMenu == "E":
        print("Gracias!")
        break;
