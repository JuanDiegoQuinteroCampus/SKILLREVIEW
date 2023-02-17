""" 4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general. """
almacen=[]
posicionmayor=0
mayorvalor=0

na = int(input("INGRESE LA CANTIDAD DE ALMACENES: "))

for i in range(na):
    nombreAlmacen=input("NOMBRE DEL ALMACEN: ")
    articulos=[]
    totalvendido=0
    narticulo = int(input("CUANTOS ARTICULOS INGRESA: "))
    for j in range (narticulo):
        tipoarticulo=input("TIPO ARTICULO: ")
        cantidadvendida=int(input("CANTIDAD VENDIDA: "))
        articulos.append(tipoarticulo)
        articulos.append(cantidadvendida)
        totalvendido=totalvendido+cantidadvendida
    print("TOTAL ALMACEN: "+nombreAlmacen,totalvendido)
    almacen.append([nombreAlmacen,articulos,totalvendido])
print(len(almacen))
for k in range(len(almacen)):
    if(k==0):
        posicionmayor=0
        mayorvalor=int(almacen[k][2])
    else:
        if(int(almacen[k][2])>mayorvalor):
            posicionmayor=k
            mayorvalor=int(almacen[k][2])

print("EL ALMACEN QUE MAS VENDIO FUE: "+almacen[posicionmayor][0],"con "+str(mayorvalor)+" items")