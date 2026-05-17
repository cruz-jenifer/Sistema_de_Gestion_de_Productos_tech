productos = []  # Lista vacía inicializada antes del bucle
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
        pass # Lógica de agregar
    elif opcion == "2":
        pass # Lógica de mostrar
    elif opcion == "3":
        pass # Lógica de buscar
    elif opcion == "4":
        pass # Lógica de eliminar
    elif opcion == "5":
        print("Saliendo del sistema...")
        ejecutando = False
    else:
        print("Opción no válida.")
