#Colas 
from collections import deque
impresiones = deque()
print ("Desea?")
print ("1. Añadir un elemento a la cola de impresion")
print ("2. Imprimir")
print ("3. Salir")
n = int(input("Ingrese su opcion: "))
while n == 1: #Repetidor del Juego
    repetir = "y"
    while repetir == "y" or repetir == "Y":
        if n == 1:
            print ("Se encontraron los siguientes archivos en la carpeta actual")
            print (impresiones)
            print ("Escriba el Nombre de su Documento si desea Añadirlo a la cola de impresion: ")
            nuevo = input()
            impresiones.append(nuevo)
            print (impresiones)
        print ("Desea ingresar otro documento y/n: ")    
        repetir = input()
    print("1. AÑADIR ELEMENTO A LA COLA DE IMPRESION")
    print("2. IMPRIMIR")
    n = int(input())
while n == 2:
    if n == 2:
        repimp = "y"
        while repimp == "y" or repimp == "Y":
            while len(impresiones)>0:
                siguiente_impresion = impresiones.popleft()
                print ("La cola queda: ", impresiones)
                print ("Se imprimio el archivo: ", siguiente_impresion)
                print ("Desea imprimir otro documento en cola y/n: ")
                repimp = input()
                if len(impresiones) == 0:
                    print("La cola de impresion esta vacia")
                    print("FIN DEL PROGRAMA")

