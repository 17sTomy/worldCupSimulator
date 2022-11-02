import time
import partidoJugador
import paises
import random
import funciones

SELECCIONES = paises.paises
fecha = 1
miEquipo = None
proximoRival = None

grupos = funciones.crearGrupos(SELECCIONES)
funciones.updateTablas(SELECCIONES, grupos)


funciones.imprimirGrupo(grupos)

if __name__ == '__main__':
    pass

funciones.clasificados(SELECCIONES)

seleccionesClasificadas = funciones.clasificados(SELECCIONES)


def eliminaciones(diccionario, seleccionesClasificadas, miEquipo, tipoPartido):
    RESULTADOS = []
    EQUIPOS = []
    equipo1 = 0
    equipo2 = 2
    i = 0
    if tipoPartido == 1:
        id_team_a = seleccionesClasificadas[0]
        id_team_b = seleccionesClasificadas[1]

        partido = lambda id_team_a, id_team_b: ((id_team_a, random.randint(0, 5-diccionario[id_team_a]["ranking"])), (id_team_b, random.randint(0, 5-diccionario[id_team_b]["ranking"])))
        resultado = partido(id_team_a, id_team_b)
        while resultado[0][1] == resultado[1][1]:
            partido = lambda id_team_a, id_team_b: ((id_team_a, random.randint(0, 5-diccionario[id_team_a]["ranking"])), (id_team_b, random.randint(0, 5-diccionario[id_team_b]["ranking"])))
            resultado = partido(id_team_a, id_team_b)
        RESULTADOS.append(resultado[0][1])
        RESULTADOS.append(resultado[1][1])
        EQUIPOS.append(id_team_a)
        EQUIPOS.append(id_team_b)
        # print(f'{diccionario[id_team_a]["nombre"]} {resultado[0][1]} - {resultado[1][1]} {diccionario[id_team_b] ["nombre"]}')
        if resultado[0][1] > resultado[1][1]:
            print(f'El gran ganador es: {diccionario[id_team_a]["nombre"]}')
        elif resultado[0][1] < resultado[1][1]:
            print(f'El gran ganador es: {diccionario[id_team_b]["nombre"]}')

    else:
        seleccionesClasificadasAux = []
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
                partido = lambda id_team_a, id_team_b: ((id_team_a, random.randint(0, 5-diccionario[id_team_a]["ranking"])), (id_team_b, random.randint(0, 5-diccionario[id_team_b]["ranking"])))
                resultado = partido(id_team_a, id_team_b)
                while resultado[0][1] == resultado[1][1]:
                    partido = lambda id_team_a, id_team_b: ((id_team_a, random.randint(0, 5-diccionario[id_team_a]["ranking"])), (id_team_b, random.randint(0, 5-diccionario[id_team_b]["ranking"])))
                    resultado = partido(id_team_a, id_team_b)
                RESULTADOS.append(resultado[0][1])
                RESULTADOS.append(resultado[1][1])
                EQUIPOS.append(id_team_a)
                EQUIPOS.append(id_team_b)
                # print(f'{diccionario[id_team_a]["nombre"]} {resultado[0][1]} - {resultado[1][1]} {diccionario[id_team_b] ["nombre"]}')
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
            print(f'{equipo1} {RESULTADOS[i]} - {RESULTADOS[i+1]} {equipo2}')
        
        seleccionesClasificadas = seleccionesClasificadasAux
        return seleccionesClasificadas

print("************OCTAVOS DE FINAL************")
octavos = eliminaciones(SELECCIONES, seleccionesClasificadas, 8, 8)
time.sleep(2)
# print(octavos)
print("************CUARTOS DE FINAL************")
cuartos = eliminaciones(SELECCIONES, octavos, 8, 4)
time.sleep(2)
# print(cuartos)
print("************SEMIFINAL************")
semifinal = eliminaciones(SELECCIONES, cuartos, 8, 2)
time.sleep(2)
# print(semifinal)
print("************FINAL************")
la_final = eliminaciones(SELECCIONES, semifinal, 8, 1)
# print(la_final)