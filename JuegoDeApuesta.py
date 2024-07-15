import random

monto_minimo = 5
saldo = 100
ganados = 0
perdidos = 0
contador_ganancias = 0
contador_perdidas = 0

print("\n---------------INICIO-DEL-JUEGO---------------\n")

apuesta = int(input("Ingrese la cantidad que desea apostar: "))

if apuesta < monto_minimo:
    print("Debe apostar al menos \$5")
    exit()
elif apuesta > saldo:
    print("Debe apostar menos de su saldo actual")
    exit()

while True:
    dado = random.randint(1, 6)

    if dado % 2 == 0:
        saldo += apuesta
        contador_ganancias += apuesta
        ganados += 1
        print("¡Número par! Ganaste el doble de tu apuesta.")
    else:
        saldo -= apuesta
        contador_perdidas -= apuesta
        perdidos += 1
        print("¡Número impar! Perdiste tu apuesta.")

    if contador_ganancias >= 500:
        print("¡Felicidades! Has alcanzado \$500 en ganancias. ¡Ganaste el juego!")
        break
    elif contador_perdidas <= -100:
        print("Tus pérdidas han superado los -\$100. El juego ha terminado.")
        break

print("\n---------------FIN-DEL-JUEGO---------------\n")
print(f"Número de ganancias: {ganados}")
print(f"Número de pérdidas: {perdidos}")
print(f"Promedio de ganancias: {contador_ganancias / ganados if ganados > 0 else 0}")
print(f"Promedio de pérdidas: {contador_perdidas / perdidos if perdidos > 0 else 0}")