""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

def luz():
    print("Mes: ", mes, "\nEstrato: ", estrato, "\nValor: ", valor, "\nDescuento: ", valores, "\nTotal a pagar: ", pago)

mes = input("Digite el mes de consumo: ")
estrato = int(input("Digite su numero de estrato: "))
while estrato >= 7:
    print("Estrato no valido")
    estrato = int(input("Digite su numero de estrato: "))
while estrato <= 0:
    print("Estrato no valido")
    estrato = int(input("Digite su numero de estrato: "))
consumo = int(input("Digite el total de kw consumido en el mes: "))

kw = 285.44
valor = kw * consumo

if estrato == 1:
    valores = (valor * 60) // 100
    pago = valor - valores
    luz()
if estrato == 2:
    valores = (valor * 50) // 100
    pago = valor - valores
    luz()
if estrato == 3:
    valores = (valor * 15) // 100
    pago = valor - valores
    luz()
if estrato == 4:
    print("Mes: ", mes, "\nEstrato: ", estrato, "\nTotal a pagar: ", valor)
if estrato == 5 or estrato == 6:
    valores = (valor * 20) // 100
    pago = valor + valores
    print("Mes: ", mes, "\nEstrato: ", estrato, "\nValor: ", valor, "\nTarifa: ", valores, "\nTotal a pagar: ", pago)
