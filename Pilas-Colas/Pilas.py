#Pilas
from collections import deque

historial=deque()


# VARIABLES DE JUEGO
import random
opciones = ["1", "2", "3"]
jugando = True
repetir = "1"

# BUCLE PRINCIPAL
print("JUEGO PIEDRA PAPEL O TIJERAS")
while repetir == "1":
	while jugando:
		opcionJugador = input("Escriba su opcion: \n1. Piedra\n2. Papel\n3. Tijeras\nSu opcion: ")
		eleccionMaquina = random.choice(opciones)
		print("La maquina responde :",eleccionMaquina)
		if opcionJugador == eleccionMaquina:
				print("EMPATE")
				continue
		
		if eleccionMaquina == "1":
			
			if opcionJugador == "2":
				print("Papel envuelve piedra! GANADOR")
				break
			if opcionJugador == "3":
				print("Piedra rompe tijeras! PERDEDOR")
				break
		
		if eleccionMaquina == "2":
			
			if opcionJugador == "3":
				print("Tijeras cortan papel! GANADOR")
				break
			if opcionJugador == "1":
				print("Papel envuelve a piedra! PERDEDOR")
				break

		if eleccionMaquina == "3":
			
			if opcionJugador == "2":
				print("Tijeras cortan papel! PERDEDOR")
				break
			if opcionJugador == "1":
				print("Piedra rompe tijeras! GANADOR")
				break
	repetir = input("Seleccione alguna opcion:   \n1. Volver a Jugar  \n2. ver historial   \n3. Salir    ")

	print(f"historial actual{historial}")


while len(historial) > 0:
	ultima_acction = historial.pop()

	print(f"Juego Mas Reciente: {ultima_acction}" )
	print(f"historial actual: {historial}")

print("FIN DEL JUEGO")

