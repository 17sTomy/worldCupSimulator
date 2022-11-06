import random
import paises #Diccionario
import partidoJugador

# FUNCTIONS

#imprimr
def pnt_tabla(tabla):
    """ Imprime la tabla de posiciones de forma más legible. """
    
    grupos = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for g in range(len(tabla)): #grupo
        print((" GRUPO "+grupos[g]+" ").center(74,"."),end='\n\n')
        for f in range(len(tabla[g])): #fila
            print(tabla[g][f][1].ljust(13), end='\t')
            for i in range(2, len(tabla[g][f])):
                print(tabla[g][f][i], end='\t')
            if f != 0:
                print()
            else:
                print(end='\n\n')
        print()

pnt_partido = lambda dic_paises, partido : print((dic_paises[partido[0][0]]["nombre"]).rjust(32)+"  "+str(partido[0][1])+" - "+str(partido[1][1])+"  "+dic_paises[partido[1][0]]["nombre"])
""" Imprime los resultados del partido de forma más legible """       

def pnt_dic(dic):                   ###### ELIMINAR ###### Prueba que funcioná la actualización del diccionario 
    for i in range (32):
        print((dic[i]["nombre"]).ljust(17) ,dic[i].get("datos"))
        if i%4 == 3:
            print()

def pnt_fixture(diccionario, lista_resultados):
    """ Imprime de forma legible los resultados de los partidos de la fecha """
    
    grupos = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for g in range(len(lista_resultados)):
        print(("GRUPO "+str(grupos[g])).center(74), end='\n\n')
        pnt_partido(diccionario, lista_resultados[g][0])
        pnt_partido(diccionario, lista_resultados[g][1])
        print()

#Metodos de ordenamiento
def ordenar_tabla(tabla):
    """ Ordená las tablas de los grupo con los paises de mayor a menor puntos. """
    
    for g in range(len(tabla)): #grupo
        for f in range(1, len(tabla[g])-1): #fila (primero-anteúltimo)
            for i in range(f+1, len(tabla[g])): #fila (segundo-último)
                if tabla[g][f][2] < tabla[g][i][2]:
                    auxiliar = tabla[g][f]
                    tabla[g][f] = tabla[g][i]
                    tabla[g][i] = auxiliar
                elif tabla[g][f][2] == tabla[g][i][2] and tabla[g][f][9] < tabla[g][i][9]:
                    auxiliar = tabla[g][f]
                    tabla[g][f] = tabla[g][i]
                    tabla[g][i] = auxiliar
def lista_menor_mayor(lista):
    """ Ordena una lista del menor al mayor. """
    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[j]
                lista[j] = lista[i]
                lista[i] = auxiliar

#Simulacion

def fecha_0(dic_paises):
    """ Crea una tabla con los grupos y datos del mundial.  """
    
    tabla = []
    cont = 0
    while cont < 32:
        for g in range (8): #grupos
            tabla.append([["ID", "País", "Pts", "PJ", "G", "E", "P", "GF", "GC", "DG"]])
            for p in range (1,5): #paises
                tabla[g].append([0]* len(tabla[g][0]))
                tabla[g][p][0] = cont
                tabla[g][p][1] = dic_paises[cont]["nombre"]
                cont += 1
    return tabla

partido = lambda  diccionario_paises, id_team_a, id_team_b : ((id_team_a, random.randint(0, 5-diccionario_paises[id_team_a]["ranking"])), (id_team_b, random.randint(0, 5-diccionario_paises[id_team_b]["ranking"])))
""" Simula el partido entre dos equipos y retorna el resultado (tuple). """

def estadisticas_partido(diccionario, partido, tabla_grupo): #tabla del grupo = matriz
    """ Actualiza las estaditicas del resultado del partido a la tabla del grupo. """
    
    # partido = ((id_pais_a, goles_a), (id_pais_b, goles_b))
    for i in range (len(partido)): #cantidad de equipos
        for j in range (1, len(tabla_grupo)): #repaso por cada fila del grupo
            if tabla_grupo[j][0] == partido[i][0]: #si conincide con el id del pais
                if partido[0-i][1] == partido[1-i][1]: #Empata
                    tabla_grupo[j][2] += 1 #Pts
                    tabla_grupo[j][3] += 1 #PJ
                    tabla_grupo[j][5] += 1 #E
                    tabla_grupo[j][7] += partido[0-i][1] #GF
                    tabla_grupo[j][8] += partido[1-i][1] #GC
                elif partido[0-i][1] > partido[1-i][1]: #Gana
                    tabla_grupo[j][2] += 3 #Pts
                    tabla_grupo[j][3] += 1 #PJ
                    tabla_grupo[j][4] += 1 #G
                    tabla_grupo[j][7] += partido[0-i][1] #GF
                    tabla_grupo[j][8] += partido[1-i][1] #GC
                    tabla_grupo[j][9] += partido[0-i][1] - partido[1-i][1] #DG
                else: #Pierde
                    tabla_grupo[j][3] += 1 #PJ
                    tabla_grupo[j][6] += 1 #P
                    tabla_grupo[j][7] += partido[0-i][1] #GF
                    tabla_grupo[j][8] += partido[1-i][1] #GC
                    tabla_grupo[j][9] += partido[0-i][1] - partido[1-i][1] #DG
                diccionario[partido[i][0]]["datos"][1:] = [tabla_grupo[j][2], tabla_grupo[j][9]] # Actualización diccionario: [Pts y DG]

def fase_grupos(diccionario, tabla, seleccion): #seleccion = Argentina
    """ Simula los partidos de cada fecha. """
    
    # Instacia previa a simulación. Imprime la tabla de cada grupo
    print((" FECHA 0 ").center(74, "|"), end='\n\n\n\n')
    pnt_tabla(tabla)
    print('\n')
    # Comienzo de simulación
    for f in range (3): #fechas
        print((" FECHA "+str(f+1)+" ").center(74, "|"), end='\n\n\n\n')
        fixture = []
        for g in range(len(tabla)): #grupos
            teams = [tabla[g][1][0], tabla[g][2][0], tabla[g][3][0], tabla[g][4][0]] 
            lista_menor_mayor(teams) # Asigna siempre la misma posición ordenada a cada pais
            #simulacion
            partido_1 = partido(diccionario, teams[0], teams[1+f])
            if f != 2:
                partido_2 = partido(diccionario, teams[3], teams[2-f])
            else:
                partido_2 = partido(diccionario, teams[1], teams[2])
            if seleccion in teams:
                for i in range(len(partido_1)):
                    if seleccion == partido_1[i][0]:
                        rival = partido_1[i-1][0]
                        print((diccionario[seleccion]["nombre"]+" "*5+"vs").rjust(37)+" "*5+diccionario[rival]["nombre"]+"\n")
                        partido_1 = partidoJugador.partidoPlayer(seleccion, rival, diccionario, "grupo")
                        partido_1 = ((seleccion, partido_1[0]), (rival, partido_1[1]))
                        print("\n\n")
                    if seleccion == partido_2[i][0]:
                        rival = partido_2[i-1][0]
                        print((diccionario[seleccion]["nombre"]+" "*5+"vs").rjust(37)+" "*5+diccionario[rival]["nombre"]+"\n")
                        partido_2 = partidoJugador.partidoPlayer(seleccion, rival, diccionario, "grupo")
                        partido_2 = ((seleccion, partido_2[0]), (rival, partido_2[1]))
                        print("\n\n")
            estadisticas_partido(diccionario, partido_1, tabla[g])
            estadisticas_partido(diccionario, partido_2, tabla[g]) 
            fixture.append([partido_1, partido_2])
        # Imprime los resultados de los partidos
        pnt_fixture(diccionario, fixture)
        # Imprime la tabla
        print('\n\n')
        ordenar_tabla(tabla)
        pnt_tabla(tabla)
        print('\n')

# MAIN PROGRAM
def simuladorFaseGrupos(diccionario, miEquipo):
    tabla_general = fecha_0(diccionario)
    fase_grupos(diccionario, tabla_general, miEquipo)

simuladorFaseGrupos(paises.paises, 8)
