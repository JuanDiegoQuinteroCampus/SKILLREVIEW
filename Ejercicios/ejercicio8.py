""" 8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

print("Algoritmo para hallar el promedio de las notas y saber si paso el semestre o no.")
print("El maximo de nota es 50 ")
print(" ")
nota1 = int(input("Digite su nota: "))
nota2 = int(input("Digite su nota: "))
nota3 = int(input("Digite su nota: "))
nota4 = int(input("Digite su nota: "))

suma = nota1 + nota2 + nota3 + nota4
promedio = suma // 4
if promedio == 50:
    print("EL estudiante aprobo el semestre")

else:
    
    if promedio == 35:
        print("EL estudiante aprobo de milagro, porque asi lo quizo Dios")

    elif promedio > 35:
        print("el estudiante aprobo")

    elif promedio < 35:
        print("Desgraciadamente reprobo el semestre")

