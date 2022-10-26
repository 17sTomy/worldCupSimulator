import relato
import random

def generarCancha():
    matriz = []
    for f in range(3):
        matriz.append([])
        for c in range(4):
            matriz[f].append(0)
    return matriz

def generarDefensores(matriz):
    for c in range(4):
        posicionJugador = random.randint(0,2)
        matriz[posicionJugador][c] = 1

    for fila in matriz:
        print(fila)

def partido():
    intentos = 3
    enPie = True
    cancha = generarCancha()
    generarDefensores(cancha)

partido()
