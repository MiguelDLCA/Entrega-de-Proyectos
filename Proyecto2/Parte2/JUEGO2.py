# VARIABLES DE JUEGO
import random
opciones = ["piedra", "papel", "tijeras"]
jugando = True
repetir = "y"

# BUCLE PRINCIPAL
print("JUEGO PIEDRA PAPEL O TIJERAS")
while repetir == "y" or repetir == "Y":
	while jugando:
		opcionJugador = input("Escriba su opcion: \nPiedra\nPapel\nTijeras\nSu opcion: ")
		eleccionMaquina = random.choice(opciones)
		print("La maquina responde :",eleccionMaquina)
		if opcionJugador == eleccionMaquina:
				print("EMPATE")
				continue
		
		if eleccionMaquina == "piedra":
			
			if opcionJugador == "papel":
				print("Papel envuelve piedra! GANADOR")
				break
			if opcionJugador == "tijeras":
				print("Piedra rompe tijeras! PERDEDOR")
				break
		
		if eleccionMaquina == "papel":
			
			if opcionJugador == "tijeras":
				print("Tijeras cortan papel! GANADOR")
				break
			if opcionJugador == "piedra":
				print("Papel envuelve a piedra! PERDEDOR")
				break

		if eleccionMaquina == "tijeras":
			
			if opcionJugador == "papel":
				print("Tijeras cortan papel! PERDEDOR")
				break
			if opcionJugador == "piedra":
				print("Piedra rompe tijeras! GANADOR")
				break
	repetir = input("Desea repetir la partida y/n: ")
print("FIN DEL JUEGO")