""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

cantidad = int(input("Cuantos empleados hay en la empresa?: "))

for v in range(cantidad):
    nombre = input("Ingrese sus nombres: ")
    apellido = input("Ingrese sus apellidos: ")
    telefono = input("Ingrese su numero de telefono: ")
    edad = input("Ingrese su edad: ")
    año = int(input("Ingrese el año en el que ingreso a la empresa: "))   

    antiguedad = 2023 - año
    print(" ")
    print(nombre + apellido, "\nTiene", antiguedad, "años de antiguaedad.")
    print(" ")
