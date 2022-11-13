import random
import time
import partidoJugador
import funciones
import paises
import faseGrupos

def eliminaciones(diccionario, seleccionesClasificadas, miEquipo, tipoPartido):
    partidoClasi = {
        8:"Octavos de Final", 
        4:"Cuartos de Final",
        2:"Semifinal",
        1:"Final"
    }
    if miEquipo not in seleccionesClasificadas and tipoPartido == 8:
        print(miEquipo, seleccionesClasificadas)
        diccionario[miEquipo]["mayorPosicion"] = "FASE DE GRUPOS"
    elif miEquipo not in seleccionesClasificadas and diccionario[miEquipo]["mayorPosicion"] == "":
        diccionario[miEquipo]["mayorPosicion"] = partidoClasi[tipoPartido*2].upper()

    RESULTADOS = []
    EQUIPOS = []
    equipo1 = 0
    equipo2 = 2
    resultado = ((0,0),(0,0))
    i = 0
    seleccionesClasificadasAux = []

    print("\n", partidoClasi[tipoPartido].center(74,"-"),"\n")

    if tipoPartido == 1:
        """ Se esta jugando la final """
        id_team_a = seleccionesClasificadas[0]
        id_team_b = seleccionesClasificadas[1]

        if (miEquipo == id_team_a) or (miEquipo == id_team_b):
                if miEquipo == id_team_a:
                    rival = id_team_b
                else:
                    rival = id_team_a
                goals = partidoJugador.partidoPlayer(miEquipo, rival, diccionario, "eliminacion")
                if goals[0] > goals[1]:
                    seleccionesClasificadasAux.append(miEquipo)
                    diccionario[miEquipo]["mayorPosicion"] = "CAMPEON"
                    print((diccionario[miEquipo]["nombre"]+" "+str(goals[0])).rjust(37),"-",str(goals[1]),diccionario[rival]["nombre"])
                    print(("Campeón del Mundo🏆: " + diccionario[miEquipo]["nombre"].upper()).center(74))
                elif goals[0] < goals[1]:
                    seleccionesClasificadasAux.append(rival)
                    diccionario[miEquipo]["mayorPosicion"] = "SUBCAMPEON"
                    print((diccionario[miEquipo]["nombre"]+" "+str(goals[0])).rjust(37),"-",str(goals[1]),diccionario[rival]["nombre"])
                    print(("Campeón del Mundo🏆: " + diccionario[rival]["nombre"].upper()).center(74))
                else:
                    seleccionesClasificadasAux.append(goals[2])
                
                diccionario[miEquipo]["datos"][2] += goals[0]
                diccionario[rival]["datos"][2] += goals[1]

        else:
            resultado = faseGrupos.partido(diccionario, id_team_a, id_team_b)
            while resultado[0][1] == resultado[1][1]:
                resultado = faseGrupos.partido(diccionario, id_team_a, id_team_b)

            print((diccionario[id_team_a]["nombre"]+" "+str(resultado[0][1])).rjust(37),"-",str(resultado[1][1]),diccionario[id_team_b] ["nombre"])
            if resultado[0][1] > resultado[1][1]:
                print(("Campeón del Mundo🏆: " + diccionario[id_team_a]["nombre"].upper()).center(74))
            elif resultado[0][1] < resultado[1][1]:
                print(("Campeón del Mundo🏆: " + diccionario[id_team_b]["nombre"].upper()).center(74))

    else:
        'Se juegan desde octavos hasta semis'
        while i < len(seleccionesClasificadas) / 2:
            id_team_a = seleccionesClasificadas[equipo1]
            id_team_b = seleccionesClasificadas[equipo2]

            if (miEquipo == id_team_a) or (miEquipo == id_team_b):
                if miEquipo == id_team_a:
                    rival = id_team_b
                else:
                    rival = id_team_a
                goals = partidoJugador.partidoPlayer(miEquipo, rival, diccionario, "eliminacion")
                if goals[0] > goals[1]:
                    seleccionesClasificadasAux.append(miEquipo)
                elif goals[0] < goals[1]:
                    seleccionesClasificadasAux.append(rival)
                else:
                    seleccionesClasificadasAux.append(goals[2])
                RESULTADOS.append(goals[0])
                RESULTADOS.append(goals[1])
                RESULTADOS.append(resultado[1][1])
                EQUIPOS.append(miEquipo)
                EQUIPOS.append(rival)
            else:
                resultado = faseGrupos.partido(diccionario, id_team_a, id_team_b)
                while resultado[0][1] == resultado[1][1]:
                    resultado = faseGrupos.partido(diccionario, id_team_a, id_team_b)

                RESULTADOS.append(resultado[0][1])
                RESULTADOS.append(resultado[1][1])
                EQUIPOS.append(id_team_a)
                EQUIPOS.append(id_team_b)
                  
                diccionario[id_team_a]["datos"][2] += resultado[0][1]
                diccionario[id_team_b]["datos"][2] += resultado[1][1]

                if resultado[0][1] > resultado[1][1]:
                    seleccionesClasificadasAux.append(seleccionesClasificadas[equipo1])
                if resultado[0][1] < resultado[1][1]:
                    seleccionesClasificadasAux.append(seleccionesClasificadas[equipo2])

            equipo1 += 4
            equipo2 += 4
            i += 1

            if i == (len(seleccionesClasificadas) / 2) / 2:
                equipo1 = 1
                equipo2 = 3
    
        for i in range(0, len(RESULTADOS)-1, 2):
            equipo1 = diccionario[EQUIPOS[i]]["nombre"]
            equipo2 = diccionario[EQUIPOS[i+1]]["nombre"]
            print((equipo1+" "+str(RESULTADOS[i])).rjust(37),"-",str(RESULTADOS[i+1]),equipo2)
        
        seleccionesClasificadas = seleccionesClasificadasAux

    time.sleep(2)

    if tipoPartido > 1:
        eliminaciones(diccionario, seleccionesClasificadas, miEquipo, tipoPartido/2)