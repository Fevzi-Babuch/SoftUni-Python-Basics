jugadores = [{'Nombre': input("Ingrese el nombre del jugador 1: "), 'Puntos': 121},
             {'Nombre': input("Ingrese el nombre del jugador 2: "), 'Puntos': 121},
             {'Nombre': input("Ingrese el nombre del jugador 3: "), 'Puntos': 121},
             {'Nombre': input("Ingrese el nombre del jugador 4: "), 'Puntos': 121}]

for ronda in range(3):
    print(f"\n-------- Ronda {ronda + 1} --------")
    for jugador in jugadores:
        if jugador['Puntos'] > 0:
            puntuacion = sum(
                int(input(f"Ingrese puntuacion del dart {i + 1} de {jugador['Nombre']}: ")) for i in range(3))
            jugador['Puntos'] -= puntuacion

        if jugador['Puntos'] <= 0:
            print(f"\n{jugador['Nombre']} ha ganado en la ronda {ronda + 1}")

    if any(jugador['Puntos'] <= 0 for jugador in jugadores):
        break

else:
    print("\nNadie ganó en 3 rondas.")