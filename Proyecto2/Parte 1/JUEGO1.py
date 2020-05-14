#GRUPO NO. 1
import random
numero = random.randint(0,30)
print("JUEGO ADIVINA EL NUMERO\nSe ha generado un nuevo numero!\n(El numero debe estar entre el rango de 0 y 30)")
continuar = "y"
while continuar == "y" or continuar == "Y": #Repetidor del Juego
    ingreso = int(input("Ingrese su respuesta: "))
    if ingreso > numero:
        print ("Su numero es muy alto")
    elif ingreso < numero:
        print ("Su numero es muy bajo")
    else:
        print("Correcto! el numero era: ", ingreso)
        numero = random.randint(0,30)
        continuar = input("Desea volver a jugar y/n: ")