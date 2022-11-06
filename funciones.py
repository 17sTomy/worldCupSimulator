import time

def progressBar(part, total, length=30):
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac: .2%}"
    return bar

def ejectProgressBar(): 
    """ Ejecuta la barra de progreso """
    for i in range(31):
        time.sleep(0.1)
        barraProgreso = progressBar(i, 30, 35)
        print(barraProgreso, end="\r")
        if i == 30:
            print(barraProgreso)


def clasificados(diccionario):
    """ Devuelve un array con todos los equipos que pasan a la siguiente ronda """
    
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