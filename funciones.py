import time
import random

def progressBar(part, total, length=30):
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac: .2%}"
    return bar

def ejectProgressBar():
    for i in range(31):
        time.sleep(0.1)
        barraProgreso = progressBar(i, 30, 35)
        print(barraProgreso, end="\r")
        if i == 30:
            print(barraProgreso)


def crearGrupos(diccionario):
    grupos = ["A","B","C","D","E","F","G","H"]
    ALL_GROUPS = []
    for grupo in grupos:
        matriz = [[],[],[],[],[]]
        elegidos = []
        for f in range(5):
            if f == 0:
                matriz[f].append(f"Grupo {grupo}")
                matriz[f].append("Puntos")
                matriz[f].append("Goles")
            else:
                for i in range(len(diccionario)):
                    if diccionario[i]["datos"][0] == grupo and diccionario[i] not in elegidos:
                        elegidos.append(diccionario[i])
                        matriz[f].append(diccionario[i]["nombre"])
                        matriz[f].append(f'   {diccionario[i]["datos"][1]}')
                        matriz[f].append(f'          {diccionario[i]["datos"][2]}')
                        break  
        ALL_GROUPS.append(matriz)
    return ALL_GROUPS

#para que funcione, los puntos los multiplica por 3
def updateTablas(diccionario, tablas):
    puntero = 0
    for grupo in tablas:
        tabla = []
        for i in range(puntero, puntero+4):
            total = (diccionario[i]["datos"][1] * 3) + diccionario[i]["datos"][2]
            tabla.append(total)
        tabla.sort(reverse=True)
        f = 1
        seleccionados = []
        for j in range(0, 4):
            for i in range(puntero, puntero+4):
                if tabla[j] == (diccionario[i]["datos"][1] * 3) + diccionario[i]["datos"][2] and diccionario[i]["nombre"] not in seleccionados:
                    seleccionados.append(diccionario[i]["nombre"])
                    c = 0
                    grupo[f][c] = diccionario[i]["nombre"]
                    c += 1
                    grupo[f][c] = '   ' + str(diccionario[i]["datos"][1])
                    c += 1
                    grupo[f][c] = '          ' + str(diccionario[i]["datos"][2])
                    f += 1
                    break
        puntero += 4


def imprimirGrupo(grupos):
    for grupo in grupos:
        for fila in grupo:
            for valor in fila:
                print("\t", valor, end=" ")
            print()
        print()


def clasificados(diccionario):
    CLASIFICADOS = []
    GRUPOS = ["A","B","C","D","E","F","G","H"]

    for grupo in GRUPOS:
        k = 0
        totalPuntos = []
        while k < len(diccionario):
            if diccionario[k]["datos"][0] == grupo:
                total = (diccionario[k]["datos"][1] * 3) + diccionario[k]["datos"][2]
                totalPuntos.append(total)
            k += 1
        totalPuntos.sort(reverse=True)
        print(totalPuntos)

        for i in range(2):
            dicc = 0
            while dicc < len(diccionario):
                total = (diccionario[dicc]["datos"][1] * 3) + diccionario[dicc]["datos"][2]
                if total == totalPuntos[i] and dicc not in CLASIFICADOS and diccionario[dicc]["datos"][0] == grupo:
                    print(diccionario[dicc]["nombre"])
                    CLASIFICADOS.append(dicc)
                    break
                dicc += 1
    print(CLASIFICADOS)
    return CLASIFICADOS