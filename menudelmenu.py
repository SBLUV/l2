opc = 0

while True:
    print("===MENU===")
    print("[1] = opcion 1")
    print("[2] = opcion 2")
    print("[3] = salir")

    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción no válida. Por favor, ingresa un número.")
        continue

    if opc == 1:
        while True:
            print("===MENU OPCION 1===")
            print("[1] = Subopcion 1")
            print("[2] = Volver al menú principal")
            opc2 = int(input("Seleccione una opción: "))
            
            if opc2 == 1:
                print("Has seleccionado la subopción 1 del menú 1.")
            elif opc2 == 2:
                break  # Vuelve al menú principal
            else:
                print("Opción no válida.")
    elif opc == 2:
        print("Has seleccionado la opción 2.")
    elif opc == 3:
        print("Saliendo...")
        break  # Sale del programa
    else:
        print("Opción no válida.")
