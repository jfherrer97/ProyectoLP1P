ciclo = "on"
ban = "si"
lista = ["hola", "Perro", "Burro", "220v"]
listaNueva = []
while ciclo == "on":
    opcion = input("\t\t\tMenú\n"
                   "1. Imprimir lista de productos actuales\n"
                   "2. Agregar producto a la lista de productos actuales\n"
                   "3. Verificar que los productos solo sean cadenas de String\n"
                   "4. Salir\n"
                   "Ingrese una opción: ")
    if opcion == "1":
        for i in lista:
            print(i)
        print()
    elif opcion == "2":
        opcionP = input("Ingrese un producto: ")
        lista.append(opcionP)
        print()
    elif opcion == "3":
        for i in lista:
            for letra in i:
                if not letra.isalpha():
                    ban = "no"
            if ban != "no":
                listaNueva.append(i)
        print(listaNueva)
        print()
    elif opcion == "4":
        ciclo = "off"
