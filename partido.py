import relato
import random
import time

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


paises = {
    0: {
        "nombre": "Holanda",
        "atq": ["Danjuma", "Depay", "De jong"],
        "dfc": ["Van Dijk", "Dunmfries", "De Vrij"],
        "arquero": "Biljow",
        "datos": ["A", 0, 0],
    },
    1: {
        "nombre": "Qatar ",
        "atq": ["Afif","Almoez Ali", "Hassan Al-Haidos"],
        "dfc": ["Hassan", "Koukhi", "Hisham"],
        "arquero": "Barshan",
        "datos": ["A", 7, 1],
    },
    2: {
        "nombre": "Ecuador",
        "atq": ["Valencia", "Mena", "Plata"],
        "dfc": ["Preciado", "Estrada", "Torres"],
        "arquero": "Alexander Dominguez",
        "datos": ["A", 7, 2],
    },
    3: {
        "nombre": "Senegal",
        "atq": ["Mane", "Sarr", "Mendy"],
        "dfc": ["Diallo", "Ciss", "Sarr"],
        "arquero": "Mendy",
        "datos": ["A", 0, 0],
    },
    4: {
        "nombre": "Iran  ",
        "atq": ["Taremi", "Azmoun", "Ezatolahi"],
        "dfc": ["Gholizadeh", "Mohammadi", "Kanani"],
        "arquero": "Beiranvand",
        "datos": ["B", 0, 0],
    },
    5: {
        "nombre": "Inglaterra",
        "atq": ["Shaw", "Stones", "Foden"],
        "dfc": ["Maguire", "Kane", "Sterling"],
        "arquero": "Pickford",
        "datos": ["B", 0, 0],
    },
    6: {
        "nombre": "Gales ",
        "atq": ["Rodon", "Williams", "Davies"],
        "dfc": ["Bale", "Moore", "James"],
        "arquero": "Hennessey",
        "datos": ["B", 0, 0],
    },
    7: {
        "nombre": "EEUU  ",
        "atq": ["Pulisic", "A. Robinson", "Pepi"],
        "dfc": ["Dest", "T. Adams", "Musah"],
        "arquero": "Steffen",
        "datos": ["B", 0, 0],
    },
    8: {
        "nombre": "Argentina",
        "atq": ["Messi", "De Paul", "Di Maria"], 
        "dfc": ["Paredes", "Romero", "Otamendi"],
        "arquero": "Dibu Martinez",
        "datos": ["C", 0, 0],
    },
    9: {
        "nombre": "Mexico",
        "atq": ["Lozano", "Corona", "Herrera"],
        "dfc": ["Sanchez", "Montes", "Vasquez"],
        "arquero": "Ochoa",
        "datos": ["C", 1, 0],
    },
    10: {
        "nombre": "Polonia",
        "atq": ["Lewandowski", "Moder", "Zielinksi"],
        "dfc": ["Glik", "Cash", "Bednarek"],
        "arquero": "Szczesny",
        "datos": ["C", 0, 0],
    },
    11: {
       "nombre": "Arabia S.",
       "atq": ["Al Faraj", "Al Muwallad", "Al Brikan"],
       "dfc": ["Al-Ghannam", "Al Amri", "Al Bulaihi"],
       "arquero": "Al Owais",
       "datos": ["C", 0, 0],
    },
    12: {
        "nombre": "Dinamarca",
        "atq": ["Kjaer", "Poulsen", "Delaney"],
        "dfc": ["Christensen", "Wass", "Skov Olsen"],
        "arquero": "Schmeichel",
        "datos": ["D", 0, 0],
    },
    13: {
        "nombre": "Australia",
        "atq": ["Rowles", "Boyle", "Behich"], 
        "dfc": ["Mabil","Hrustic", "Wright"],
        "arquero": "Ryan",
        "datos": ["D", 0, 0],
    },
    14: {
        "nombre": "Francia",
        "atq": ["Mpabbe", "Pogba","Griezmann"],
        "dfc": ["Varane", "Benzema", "Kounde"],
        "arquero": "Lloris",
        "datos": ["D", 0, 0],
    },
    15: {
        "nombre": "Tunez ",
        "atq": ["Jaziri", "Khazri", "Msakni"],
        "dfc": ["Talbi", "Maaloul", "Ghandri"],
        "arquero": "Ben Said",
        "datos": ["D", 0, 0],
    },
    16: {
        "nombre": "Alemania",
        "atq": ["T. Müller", "T. Werner", "Gnabry"],
        "dfc": ["Sule", "Tisch", "Raum"],
        "arquero": "Neuer",
        "datos": ["E", 0, 0],
    },
    17: {
        "nombre": "Costa Rica",
        "atq": ["Oviedo", "Calvo", "Tejeda"],
        "dfc": ["Torres" , "Campbell", "Fuller"],
        "arquero": "Keylor Navas",
        "datos": ["E", 0, 0],
    },
    18: {
        "nombre": "España",
        "atq": ["Pedri", "Morata", "Dani Olmo"],
        "dfc": ["Jordi Alba", "Laporte", "Eric Garcia"],
        "arquero": "Unai Simon",
        "datos": ["E", 0, 0],
    },
    19: {
        "nombre": "Japon ",
        "atq": ["Minamino","Tanaka","J. Ito"],
        "dfc": ["Tomiyasu", "Nagatomo", "Sakai"],
        "arquero": "Gonda",
        "datos": ["E", 0, 0],
    },
    20: {
        "nombre": "Belgica",
        "atq": ["Kevin De Bruyne", "Eden Hazard", "De Bruyne"],
        "dfc": ["Denayer", "Vertoghen", "Witsel"],
        "arquero": "Courtois",
        "datos": ["F", 0, 0],
    },
    21: {
        "nombre": "Canada",
        "atq": ["Larin", "Laryea", "Buchanan"],
        "dfc": ["Miller", "S. Vitoria", "Johnston"],
        "arquero": "Borjan",
        "datos": ["F", 0, 0],
    },
    22: {
        "nombre": "Marruecos",
        "atq": ["Louza","Amallah","El Kaabi"],
        "dfc": ["Aguerd", "Masina", "Saiss"],
        "arquero": "Bounou",
        "datos": ["F", 0, 0],
    },
    23: {
        "nombre": "Croacia",
        "atq": ["Kovacic", "Modric", "Juranovic"],
        "dfc": ["Vlasic", "Perisic", "Sosa"],
        "arquero": "Grbic",
        "datos": ["F", 0, 0],
    },
    24: {
        "nombre": "Brasil",
        "atq": ["Neymar Jr.", "Vini Jr.", "Paqueta"],
        "dfc": ["Casemiro", "Danilo", "Thiago Silva"],
        "arquero": "Alisson",   
        "datos": ["G", 0, 0],
    },
    25: {
        "nombre": "Camerun",
        "atq": ["Fai","Ondoua", "Ngadeu"], 
        "dfc": ["Aboubakar", "Choupo-Moting", "Castelleto"],
        "arquero": "Onana",
        "datos": ["G", 0, 0],
    },
    26: {
        "nombre": "Serbia",
        "atq": ["Kostic", "Mitrovic", "Tadic"],
        "dfc": ["Pavlovic", "Veljkovic", "Milenkovic"],
        "arquero": "Rajkovic",
        "datos": ["G", 0, 0],
    },
    27: {
        "nombre": "Suiza ",
        "atq": ["Zakaria", "Vargas", "Okafor"],
        "dfc": ["Mbabu", "Akanji", "Rodriguez"],
        "arquero": "Sommer",
        "datos": ["G", 0, 0],
    },
    28: {
        "nombre": "Corea del Sur",
        "atq": ["Min-Jae", "Jin-Su", "Hee-Chan"],
        "dfc": ["Jae-Sung", "Young-Gwon", "Lee young"],
        "arquero": "Seung-Gyu",
        "datos": ["H", 0, 0],
    },
    29: {
        "nombre": "Ghana ",
        "atq": ["Kudus", "Thomas Partey", "Fatawu"],
        "dfc": ["Amartey","Baba", "Djiuku"],
        "arquero": "Wollacott",
        "datos": ["H", 0, 0],
    },
    30: {
        "nombre": "Portugal",
        "atq": ["Ronaldo", "Jota", "Fernades"],
        "dfc": ["Dias", "Pepe", "Cancelo"],
        "arquero": "Costa",
        "datos": ["H", 0, 0],
    },    
    31: {
        "nombre": "Uruguay",
        "atq": ["Suarez", "Nuñez", "Valverde"],
        "dfc": ["Gimenez", "Godin", "Araujo"],
        "arquero": "Rochet",
        "datos": ["H", 10, 0],
    },
}

def imprimirComentario(equipo, jugador, tipoFrase, diccionario):
    randomPlayer = diccionario[equipo][jugador][random.randint(0, 2)].upper()
    relatoRandom = random.randint(0, len(tipoFrase)-1)
    print(tipoFrase[relatoRandom] + " " + randomPlayer + "...")

def imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival):
    print(f'{diccionario[miEquipo]["nombre"]} {golesAFavor} - {golesEnContra} {diccionario[rival]["nombre"]}')

def gritarGol():
    relatoRandom = random.randint(0, len(relato.frases_gol)-1)
    print(relato.frases_gol[relatoRandom])


def jugadaAtqDfc(golesAFavor, golesEnContra, diccionario, miEquipo, rival):
    cancha = generarCancha()
    generarDefensores(cancha)
    enPie = True
    enPieRival = True
    index = 0
    while index < 4 and enPie:
        direccion = input("Elija si quiere ir por la izquierda, derecha, o por el medio (I / D / M): ").upper()
        enPie = gambeta(direccion, cancha, index, enPie)
        if enPie:
            imprimirComentario(miEquipo, "atq", relato.frases_atq, diccionario)
        else:
            imprimirComentario(rival, "dfc", relato.frases_dfc, diccionario)
        index += 1
        for fila in cancha:
            print(fila)
    print()
    if enPie:
        golesAFavor += 1
        gritarGol()
        imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival)
    print("************************************************************************")

    index = 0
    while index < 4 and enPieRival:
        POSICIONES = ["I", "D", "M"]
        atacanteRandom = POSICIONES[random.randint(0, 2)]
        print(atacanteRandom)
        direccion = input("Elija donde colocar al defensor (I / D / M): ").upper()
        enPieRival = direccion != atacanteRandom
        if enPieRival:
            imprimirComentario(rival, "atq", relato.frases_atq, diccionario)
        else:
            imprimirComentario(miEquipo, "dfc", relato.frases_dfc, diccionario)
        index += 1
    if enPieRival:
        golesEnContra += 1
        gritarGol()
        imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival)

    return golesAFavor, golesEnContra


def partido(miEquipo, rival, diccionario, tipoPartido): 
    intentos = 3
    golesAFavor = 0
    golesEnContra = 0
    while intentos > 0:
        goles = jugadaAtqDfc(golesAFavor, golesEnContra, diccionario, miEquipo, rival)
        golesAFavor = 0
        golesAFavor += goles[0]
        golesEnContra = 0
        golesEnContra += goles[1]
        intentos -= 1
        print("************************************************************************")

    if golesAFavor == golesEnContra:
        if tipoPartido == "grupo":
            print()
            print("Pita el arbitro, se terminó el partido en EMPATE...")
            imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival)
        else:
            print("Nos vamos al TIEMPO EXTRA...")
            print()  
            intentos = 1
            while intentos > 0:
                goles = jugadaAtqDfc(golesAFavor, golesEnContra, diccionario, miEquipo, rival)
                golesAFavor = 0
                golesAFavor += goles[0]
                golesEnContra = 0
                golesEnContra += goles[1]
                intentos -= 1
                print("************************************************************************")
                if golesAFavor == golesEnContra:
                    print("NOS VAMOS A LOS PENALES...")
                    time.sleep(1)
                    resultadoRandom1 = random.randint(0, 5)
                    resultadoRandom2 = random.randint(0, 5)
                    while resultadoRandom1 == resultadoRandom2:
                        resultadoRandom1 = random.randint(0, 5)
                        resultadoRandom2 = random.randint(0, 5)
                    print()
                    if resultadoRandom1 > resultadoRandom2:
                        print(f'Señoras y señores, ha ganado {diccionario[miEquipo]["nombre"]} a {diccionario[rival]["nombre"]} por penales: {resultadoRandom1} - {resultadoRandom2}')
                        print()
                    else:
                        print(f'Señoras y señores, ha ganado {diccionario[rival]["nombre"]} a {diccionario[miEquipo]["nombre"]} por penales: {resultadoRandom2} - {resultadoRandom1}')
                        print()
                        print("************************************************************************")
                else:
                    print()
                    print("Pita el arbitro, se terminó el tiempo extra...")
                    imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival)
    else:
        print("Pita el arbitro, se terminó el partido...")
        imprimirMarcador(golesAFavor, golesEnContra, diccionario, miEquipo, rival)

partido(8, 9, paises, "gru")



