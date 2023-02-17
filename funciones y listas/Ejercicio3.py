""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """
def registroCiclistas():
    sueldoKilometro = []
    numerokilometro = []
    nkmLider = []
    for i in range(1):
        sueldoxKm = int(input("Digite el sueldo por km recorrido: "))
        sueldoKilometro.append(sueldoxKm)
        nKm = int(input("Número de km: "))
        numerokilometro.append(nKm)
        kmCamisetaLider = int(input("Ingrese número de kilómetros recorridos con la camisa lider: "))
        nkmLider.append(kmCamisetaLider)
    return sueldoKilometro, numerokilometro, nkmLider
option = -1

def valorTotal(sueldoKilometro, numerokilometro, nkmLider):
    if(nkmLider[0] > 1800):
        sueldoNuevo = ((sueldoKilometro[0] * 25) / 100) + sueldoKilometro[0]
        valorTotalCamisaLider = sueldoNuevo * nkmLider[0]
        kmRestantes = numerokilometro[0] - nkmLider[0]
        valorTotal = valorTotalCamisaLider + (sueldoKilometro[0] * kmRestantes)
        print("El valor total a pagar por haber recorrido más de 1800 km  con la camiseta lider es: ",valorTotal)
        if(numerokilometro[0] >= 3277):
            print("Felicidades, eres ganador de 700 MILLONES por haber recorrido los 3277 km")
        else:
            print("El valor total a pagar por haber recorrido más de 1800 km  con la camiseta lider es: ",valorTotal)
    elif (numerokilometro[0] >= 3277):
            print("Felicidades, eres ganador de 700 MILLONES por haber recorrido los 3277 km")
            print("Incluyendo su sueldo por kilometros recorridos: ",(sueldoKilometro[0] * numerokilometro[0]))
    else: 
        print("Felicidades, eres ganador de 700 MILLONES por haber recorrido los 3277 km")

while(option != 0):
    print("1. Ingresar datos")
    print("2. Valor a pagar total")

    option = int(input("Ingrese la opcion: "))

    if(option == 1):
        sueldoKilometro, numerokilometro, nkmLider = registroCiclistas()
    elif(option == 2):
        valorTotal(sueldoKilometro, numerokilometro, nkmLider)