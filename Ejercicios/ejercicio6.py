""" 6. En sus propias palabras, qué son las funciones
preconstruidas y proporcione 2 ejemplos. """

print(f"las funciones preconstruidas son: Las que python ya tiene en su base de datos")


def listas():
    listaN = []
    cantidad = int(input("Digite la cantidad de numeros que desea colocar: "))
    for i in range(cantidad):
        listaN.append(int (input("Digite el numero: ")))
    return listaN

def maximo(listaN):
    print(max(listaN))

def minimo(listaN):
    print(min(listaN))

option = -1
while option != 0:
    print(" ")
    print("---------- OPCIONES ----------")
    print("1. Crear lista con numeros.")
    print("2. Hallar el numero maximo de los numeros que ingresaste.")
    print("3. Hallar el numero minimo de los numeros que ingresaste.")
    print("4. Cerrar programa")
    print("-------------------------------")
    print(" ")
    option = int(input("Digite la opcion que desea: "))

    if option == 1:
        listaN = listas()
    elif option == 2:
        from os import system
        system("clear")
        maximo(listaN)
    elif option == 3:
        from os import system
        system("clear")
        minimo(listaN)
    elif option == 4:
        from os import system
        system("clear")
        break