import time

def progressBar(part, total, length=30):
    """
    Crea la barra de progreso
    """
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"{'⚽'*completed}{'🏆'*missing}{frac: .2%}"
    return bar

def ejectProgressBar(): 
    """
    Imprime la barra de progreso
    """
    """ Ejecuta la barra de progreso """
    for i in range(31):
        time.sleep(0.1)
        barraProgreso = progressBar(i, 30, 35)
        print(barraProgreso, end="\r")
        if i == 30:
            print()


def clasificados(tabla_general):
    """ 
    Devuelve un array con todos los equipos que pasan a la siguiente ronda
    """
    
    CLASIFICADOS = []
    for grupo in range(len(tabla_general)):
        for fila in range(1, 3):
            CLASIFICADOS.append(tabla_general[grupo][fila][0])
    
    return CLASIFICADOS