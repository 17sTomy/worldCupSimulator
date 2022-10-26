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

def crearGrupo(diccionario, grupo):
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
    return matriz

def imprimirGrupo(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


