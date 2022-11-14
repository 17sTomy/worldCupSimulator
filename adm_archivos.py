from paises import paises
from os import remove

def equipos_elegibles(equipos_disponibles):
    """
    Esta funcion recibe una lista de pasises por parametro
    y los imprime por pantalla en tres columnas para que
    las mismas puedan ser visualizadas por el usuario.
    """
    
    piso = 0
    techo = 4

    print("Puede elegir entre los siguientes equipos: \n")

    for x in range(8):
        for equipo in equipos_disponibles[piso:techo]:
            if len(equipo) >= 7:
                print("\t", equipo, end="")
            else:
                print("\t", equipo, end="\t")
        print()
        piso += 4
        techo += 4
    print()

def seleccionar_equipo(dic_fase_de_grupos):
    
    """
    Esta funcion recibe or parametro un diccionario
    con el estado inicial del juego. le pide el usuario
    que ingrese por pantalla su nombre y el equipo que
    elije. La funcion retorna una tupola con el nombre de
    usuario y la clave del equip que eligio en el diccionario.
    """
    
    PAIS = "nombre"
    usuario = input("Ingrese su nombre de usuario: ")
    
    print("\nBIENVENIDO {} \n".format(usuario))
    
    equipos_disponibles = [clave[PAIS] for clave in dic_fase_de_grupos.values()]
    
    equipos_elegibles(equipos_disponibles)
    equipo_elegido = input("\n         Ingrese por favor su equipo elegido (Tenga en cuenta respetar las mayusculas, minusculas y tildes):")
    
    while equipo_elegido not in equipos_disponibles:
        print("\n         ¡ERROR! NO SE ENCONTRO A {} EN LA BASE DE DATOS DEL JUEGO.".format(equipo_elegido))
        equipo_elegido = input("         Ingrese nuevamente su equipo elegido (Tenga en cuenta respetar las mayusculas, minusculas y tildes): ")
        
    return usuario,equipos_disponibles.index(equipo_elegido)



def cargar_progreso(mundial, usuario, equipo):
    
    """
    Esta funcion recibe como parametro el
    nombre del usuario que juega actualmente
    y el diccionario del mundial con el estado
    de los equipos actualizado. crea un archivo
    CSV 'partida_guardada_USUARIO_EQUIPO.csv'donde guarda
    los datos de todos los equipos en un a linea
    para cada uno.
    """
    
    nombre_del_archivo = "partidasGuardadas/partida_guardada_{}_{}.csv".format(usuario, equipo)
    partida_guardada = open(nombre_del_archivo, "w")
    GRUPO, PUNTOS, GOLES = 0, 1, 2
    JUGADOR_1, JUGADOR_2, JUGADOR_3 = 0,1,2

    
    print("Tu progreso en la competicion fue genial. ¡Esperamos que vuelvas pronto!")
    print("\n\n ¡IMPORTANTE! Tené en cuenta que si un mismo usuario decide empezar y guardar otra partida con el mismo equipo, la primera partida se va a pisar y se va a perder el progreso de la misma.")
    
    for equipo in mundial:
        partida_guardada.write(str(equipo) + "," + mundial[equipo]["nombre"] + "," + mundial[equipo]["atq"][JUGADOR_1] +
                               "," + mundial[equipo]["atq"][JUGADOR_2] + "," + mundial[equipo]["atq"][JUGADOR_3] +
                               "," + mundial[equipo]["dfc"][JUGADOR_1] + "," + mundial[equipo]["dfc"][JUGADOR_2] +
                               "," + mundial[equipo]["dfc"][JUGADOR_3] + "," + mundial[equipo]["arquero"] +
                               "," + mundial[equipo]["datos"][GRUPO] + "," + str(mundial[equipo]["datos"][PUNTOS]) +
                               "," + str(mundial[equipo]["datos"][GOLES]) + "," + str(mundial[equipo]["ranking"]) +
                               "," + mundial[equipo]["mayorPosicion"] + "\n")
        
    partida_guardada.close()


def retomar_partida(usuario, equipo):
    
    """
    Recibe como parametro el nombre del usuario
    que quiere retomar la partida. Abre el archivo
    que contiene la partuda guardada y escribe su
    contenido en un diccionario. Borra el arhivo
    del que se extrajeron los datos y posteriormente
    devuelve el diccionario.
    """
    
    CLAVE, EQUIPO, ATQ_1, ATQ_2, ATQ_3 = 0,1,2,3,4
    DFC_1, DFC_2, DFC_3, ARQUERO, GRUPO = 5,6,7,8,9
    PUNTOS, GOLES, RANKING, MAYOR_POSICION = 10,11,12,13
    mundial = {}
    nombre_del_archivo = "partidasGuardadas/partida_guardada_{}_{}.csv".format(usuario, equipo)
    partida_retomada = open(nombre_del_archivo, "r")
    
    for equipo in partida_retomada:
        linea = equipo.rstrip("\n").split(",")
        clave = int(linea[CLAVE])
        equipo = linea[EQUIPO]
        atq_1 = linea[ATQ_1]
        atq_2 = linea[ATQ_2]
        atq_3 = linea[ATQ_3]
        dfc_1 = linea[DFC_1]
        dfc_2 = linea[DFC_2]
        dfc_3 = linea[DFC_3]
        arquero = linea[ARQUERO]
        grupo = linea[GRUPO]
        puntos = int(linea[PUNTOS])
        goles = int(linea[GOLES])
        ranking = int(linea[RANKING])
        mayor_posicion = linea[MAYOR_POSICION]
        
        mundial[clave] = {}
        mundial[clave]["nombre"] = equipo
        mundial[clave]["atq"] = [atq_1, atq_2, atq_3]
        mundial[clave]["dfc"] = [dfc_1, dfc_2, dfc_3]
        mundial[clave]["arquero"] = arquero
        mundial[clave]["datos"] = [grupo, puntos, goles]
        mundial[clave]["ranking"] = ranking
        mundial[clave]["mayorPosicion"] = mayor_posicion
        
    partida_retomada.close()
    remove(nombre_del_archivo)
    
    return mundial


def cargar_historial(mundial, usuario, equipo):
    
    """
    Esta funcion guarda el progreso de la
    partida de cada usuario con cada equipo
    en un archivo 'historial.csv'.
    """
    
    fases_del_mundial = {"FASE DE GRUPOS": 32, "OCTAVOS DE FINAL": 16, "CUARTOS DE FINAL": 8,
                         "SEMIFINAL": 4, "SUBCAMPEON": 2, "CAMPEON": 1}
    
    historial = open("historial.csv", "a")
    historial.write(usuario + "," + str(fases_del_mundial[mundial[equipo]["mayorPosicion"]]) +
                    "," + mundial[equipo]["nombre"] + "," + str(mundial[equipo]["ranking"]) + "\n")
    historial.close()
    
    pass
    

def mostrar_historial():
    
    """
    Esta funcion lee el archivo 'historial.csv'
    que contiene registradas las artidas de todos
    los usuarios e imprime un ranking ordenado
    por los siguientes criterios:
        1) Instancia a la que se llegó.
        2) Equipo con el que se jugó.
    """
    
    USUARIO, INSTANCIA, EQUIPO, RANKING = 0,1,2,3
    fases_del_mundial = {32: "FASE DE GRUPOS", 16: "OCTAVOS DE FINAL", 8: "CUARTOS DE FINAL",
                         4: "SEMIFINAL", 2: "SUBCAMPEON", 1: "CAMPEON"}
    ranking = []
    puesto = 1
    historial = open("historial.csv", "r")
    
    for linea in historial:
        partida = linea.rstrip("\n").split(",")
        partida[RANKING] = int(partida[RANKING])
        partida[INSTANCIA] = int(partida[INSTANCIA])
        ranking.append(partida)
    
    ranking_ordenado = sorted(ranking, key = lambda juego: (juego[INSTANCIA], -juego[RANKING]))
    
    print()
    print("\t¡RANKING HISTORICO DE PARTIDAS!\n")
    
    for juego in ranking_ordenado:
        print("Puesto", puesto, "{}, Equipo: {}. Llegó hasta {}.".format(juego[USUARIO], juego[EQUIPO], fases_del_mundial[int(juego[INSTANCIA])]))
        puesto += 1
    
    historial.close()


def partida(diccionario):

    """
    Esta funcion determina si hay que retomar
    o no una partida dependiendo del usuario
    y equipo que se estan logueando.
    """
    
    usuario, equipo = seleccionar_equipo(diccionario)
    
    try:
        nombre_del_archivo = "partidasGuardadas/partida_guardada_{}_{}.csv".format(usuario, equipo)
        partida_retomada = open(nombre_del_archivo)
        partida_retomada.close()
    
    except FileNotFoundError:
        print("¡MUCHA SUERTE EN TU NUEVA PARTIDA!")
        diccionario = paises
    
    else:
        print("\nParece que hay una partida ya guardada con tu usuario y equipo elegidos")
        retomar = input("¿Desea retomar la partida guardada? (Ingrese cualquier tecla para retomar la partida, sino ingrese ENTER): ").upper()
        
        if retomar:
            diccionario = retomar_partida(usuario, equipo)
        else:
            diccionario = paises
    
    return diccionario, usuario, equipo
