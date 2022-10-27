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

def gambeta(direccion, matriz, posicion, enPie):
    if direccion == "I" and matriz[0][posicion] != 1:
        matriz[0][posicion] = "P"
    elif direccion == "M" and matriz[1][posicion] != 1:
        matriz[1][posicion] = "P"
    elif direccion == "D" and matriz[2][posicion] != 1:
        matriz[2][posicion] = "P"
    else:
        enPie = False
    return enPie


def partido(miEquipo, rival, diccionario):
    intentos = 3
    golesAFavor = 0
    golesEnContra = 0
    while intentos > 0:
        cancha = generarCancha()
        generarDefensores(cancha)
        enPie = True
        index = 0
        while index < 4 and enPie:
            direccion = input("Elija si quiere ir por la izquierda, derecha, o por el medio (I / D / M): ").upper()
            enPie = gambeta(direccion, cancha, index, enPie)
            index += 1
            for fila in cancha:
                print(fila)

        #funcion para pegarle al arco si enPie == True

        break #esto esta para que se termine, despues sacarlo

        # funcion de defensa

        intentos -= 1


partido()
