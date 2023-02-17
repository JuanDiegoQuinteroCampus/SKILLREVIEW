""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, """

def crearA():
    grupoA=[]
    campersA = int(input("Introdusca la cantidad de campers:"))
    for i in range(campersA):
        grupoA.append (input("Introdusca el nombre del camper:"))
    return grupoA

def imprimirA(grupoA):
    for i in range(len(grupoA)):
        print(grupoA[i])
    
def agregarA(grupoA):
    agregar=input("Ingrese el nombre del camper que desea agregar:")
    grupoA.append(agregar)

def eliminarA(grupoA):
    eliminar=input("Ingrese el nombre del camper a eliminar: ")
    grupoA.remove (eliminar)
    

def ordenarA(grupoA):
    grupoA.sort()
    

def buscarA(grupoA):
    buscar=input("Ingrese el nombre del camper que desea buscar: ")
    if buscar in grupoA:
        print("")
        print("El camper si se encuentra en el grupo ARTEMIS") 

    else:
        print("")
        print("El camper no se encuentra en el grupo ARTEMIS")    
    

def crearB():
    grupoB=[]
    campersB = int(input("Introdusca la cantidad de campers:"))
    for i in range(campersB):
        grupoB.append (input("Introdusca el nombre del camper:"))
    return grupoB

def imprimirB(grupoB):
    for i in range(len(grupoB)):
        print(grupoB[i])
    
def agregarB(grupoB):
    agregar=input("Ingrese el nombre del camper que desea agregar:")
    grupoB.append(agregar)

def eliminarB(grupoB):
    eliminar=input("Ingrese el nombre del camper a eliminar: ")
    grupoB.remove (eliminar)
    

def ordenarB(grupoB):
    grupoB.sort()
    

def buscarB(grupoB):
    buscar=input("Ingrese el nombre del camper que desea buscar: ")
    if buscar in grupoB:
        print("")
        print("El camper si se encuentra en el grupo SPUTNICK") 

    else:
        print("")
        print("El camper no se encuentra en el grupo ARTEMIS")   


option1=-1
while option1 != 0:

        print("")
        print("---------------------MENU--------------------")
        print("1. CREAR GRUPO ARTEMIS:")
        print("1.1 LISTAR CAMPERS DE ARTEMIS")
        print("1.2 AGREGAR CAMPERS A ARTEMIS")
        print("1.3 ELIMINAR CAMPERS DE ARTEMIS")
        print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
        print("1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS")
        print("2. CREAR GRUPO SPUTNIK: ")
        print("2.1 LISTAR CAMPERS DE SPUTNIK: ")
        print("2.2 AGREGAR CAMPERS A SPUTNIK: ")
        print("2.3 ELIMINAR CAMPERS DE SPUTNIK: ")
        print("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
        print("2.5 BUSCAR CAMPER EN LA LISTA DEL GRUPO DE SPUTNIK")
       
        option= float(input("Digite la opcion deseada:"))
        if option == 1:
            grupoA=crearA()
        elif option==1.1:
            imprimirA(grupoA)
        elif option==1.2:
            agregarA(grupoA)
        elif option==1.3:
            eliminarA(grupoA)
        elif option==1.4:
            ordenarA(grupoA)
        elif option == 1.5:
            buscarA(grupoA)
        elif option == 2:
            grupoB= crearB()
        elif option == 2.1:
            imprimirB(grupoB)
        elif option == 2.2:
            agregarB(grupoB)
        elif option == 2.3:
            eliminarB(grupoB)
        elif option == 2.4:
            ordenarB(grupoB)
        elif option == 2.5:
            buscarB(grupoB)
            
            
        






 