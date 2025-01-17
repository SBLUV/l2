opc = 0

while True:
    print ("===MENU===")
    print("[1] = opcion 1")
    print("[2] = opcion 2")
    print("[3] = salir")

    try:
        opc = int (input("sleccione una opcion"))

    except ValueError:
        print("opcion no valida")

    if opc == 1:
        print("opcion 1")
    elif opc == 2:
        print("opcion 2")
    elif opc == 3:
        break
