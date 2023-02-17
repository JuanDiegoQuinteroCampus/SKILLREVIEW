""" 2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

num_atletas = 3
atletas = []

# Pedir nombres y marcas de los atletas
for i in range(num_atletas):
    nombre = input("Nombre del atleta " + str(i+1) + ": ")
    marca = float(input("Marca del salto en metros del atleta " + str(i+1) + ": "))
    atletas.append((nombre, marca))

# Ordenar lista de atletas en orden descendente de acuerdo con la marca
atletas.sort(key=lambda x: x[1], reverse=True)

# Imprimir resultado
print("La atleta campeona es:", atletas[0][0])

if atletas[0][1] > 15.50:
    print("¡Ha roto el récord y recibirá un pago de 500 millones!")
else:
    print("No ha roto el récord.")