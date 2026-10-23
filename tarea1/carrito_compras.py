def carrito_compras_interactivo():
    carrito = []
    print("--- CREACIÓN DE LA LISTA DE COMPRAS ---")
    print("Ingrese cinco productos para la semana:")
    for i in range(1, 6):
        producto = input(f"Ingrese el producto {i}: ")
        carrito.append(producto)
    print("\nCarrito inicial:", carrito)
    nuevo_primero = input("\nIngrese un producto extra para insertar en la primera posición: ")
    carrito.insert(0, nuevo_primero)
    producto_acabado = input("¿Qué producto se ha acabado y desea eliminar del carrito?: ")
    if producto_acabado in carrito:
        carrito.remove(producto_acabado)
        print(f"Se ha eliminado '{producto_acabado}' del carrito.")
    else:
        print(f"El producto '{producto_acabado}' no estaba en la lista.")
    print("\n--- RESUMEN DEL CARRITO ---")
    print(f"Carrito completo: {carrito}")
    print(f"Primer artículo: {carrito[0]}")
    print(f"Último artículo: {carrito[-1]}")
    print(f"Total de productos en el carrito: {len(carrito)}")
    consulta = input("\nIngrese un producto que desee verificar si quedó en el carrito: ")
    if consulta in carrito:
        print(f"Verificación: El producto '{consulta}' SÍ se encuentra en el carrito.")
    else:
        print(f"Verificación: El producto '{consulta}' NO se encuentra en el carrito.")
# Las listas son ideales para este problema porque permiten almacenar colecciones 
# ordenadas de elementos que cambian dinámicamente mediante inserciones y eliminaciones.
# Además, facilitan el acceso por índices y la iteración secuencial de los productos.
carrito_compras_interactivo()