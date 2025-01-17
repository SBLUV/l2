nombre = "hola soy pedro"
contador = -1
print (nombre[4])

for i in nombre:
    contador += 1
    if i == 'p':
        print("encuentra la p, en la posicion", contador)
    if i == 'y':
        print("encontre la y")
        #break