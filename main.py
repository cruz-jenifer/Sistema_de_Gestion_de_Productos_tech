productos = []  # INICIALIZACION
ejecutando = True

while ejecutando:
    print("\n--- Sistema de Gestión Básica De Productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    if opcion == "1":
        # AGREGAR PRODUCTO
        nombre = ""
        while nombre == "":
            nombre = input("Ingrese el nombre del producto: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                
        categoria = ""
        while categoria == "":
            categoria = input("Ingrese la categoría del producto: ").strip()
            if categoria == "":
                print("La categoría no puede estar vacía.")
                
        precio = 0
        while precio <= 0:
            entrada_precio = input("Ingrese el precio (solo números enteros positivos): ").strip()
            if entrada_precio.isdigit():
                precio = int(entrada_precio)
                if precio <= 0:
                    print("El precio debe ser mayor a 0.")
            else:
                print("Entrada no válida. Ingrese un número entero.")
                
        # CREACION DE DICCIONARIO
        nuevo_producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        
        # AGREGAR A LISTA
        productos.append(nuevo_producto)
        print(f"¡Producto '{nombre}' agregado correctamente!")
    elif opcion == "2":
        # MOSTRAR PRODUCTOS
        if len(productos) == 0:
            print("No hay productos registrados en el sistema.")
        else:
            print("\n--- Lista de Productos Registrados ---")
            for i in range(len(productos)):
                prod = productos[i] 
                print(f"Producto {i + 1}:")
                # DETALLES DEL PRODUCTO
                print(f"  • Nombre: {prod['nombre']}")
                print(f"  • Categoría: {prod['categoria']}")
                print(f"  • Precio: ${prod['precio']}")
                print("-" * 30)
    elif opcion == "3":
        pass  # BUSCAR PRODUCTO
    elif opcion == "4":
        pass  # ELIMINAR PRODUCTO
    elif opcion == "5":
        # SALIR
        print("Saliendo del sistema...")
        ejecutando = False
    else:
        # ERROR
        print("Opción no válida.")
