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

def clasificados2(diccionario):
    """ 
    Devuelve un array con todos los equipos que pasan a la siguiente ronda
    """
    GRUPOS = ["A","B","C","D","E","F","G","H"]
    CLASIFICADOS = []
    for grupo in GRUPOS:
        k = 0
        totalPuntos = []
        while k < len(diccionario):
            if diccionario[k]["datos"][0] == grupo:
                total = diccionario[k]["datos"][1] 
                totalPuntos.append(total)
            k += 1
        totalPuntos.sort(reverse=True)
        for i in range(2):
            dicc = 0
            while dicc < len(diccionario):
                total = diccionario[dicc]["datos"][1] 
                if total == totalPuntos[i] and dicc not in CLASIFICADOS and diccionario[dicc]["datos"][0] == grupo:
                    CLASIFICADOS.append(dicc)
                    break
                dicc += 1
                
    return CLASIFICADOS


# paises = {
#     0: {
#         "nombre": "Qatar",
#         "atq": ["Afif","Almoez Ali", "Hassan Al-Haidos"],
#         "dfc": ["Hassan", "Koukhi", "Hisham"],
#         "arquero": "Barshan",
#         "datos": ["A", 5, 0], 
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     1: {
#         "nombre": "Ecuador",
#         "atq": ["Valencia", "Mena", "Plata"],
#         "dfc": ["Preciado", "Estrada", "Torres"],
#         "arquero": "Alexander Dominguez",
#         "datos": ["A", 9, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     2: {
#         "nombre": "Senegal",
#         "atq": ["Mane", "Sarr", "Mendy"],
#         "dfc": ["Diallo", "Ciss", "Sarr"],
#         "arquero": "Mendy",
#         "datos": ["A", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     3: {
#         "nombre": "Paises Bajos",
#         "atq": ["Danjuma", "Depay", "De jong"],
#         "dfc": ["Van Dijk", "Dunmfries", "De Vrij"],
#         "arquero": "Biljow",
#         "datos": ["A", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     4: {
#         "nombre": "Inglaterra",
#         "atq": ["Shaw", "Stones", "Foden"],
#         "dfc": ["Maguire", "Kane", "Sterling"],
#         "arquero": "Pickford",
#         "datos": ["B", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     5: {
#         "nombre": "Iran",
#         "atq": ["Taremi", "Azmoun", "Ezatolahi"],
#         "dfc": ["Gholizadeh", "Mohammadi", "Kanani"],
#         "arquero": "Beiranvand",
#         "datos": ["B", 0, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     6: {
#         "nombre": "EEUU",
#         "atq": ["Pulisic", "A. Robinson", "Pepi"],
#         "dfc": ["Dest", "T. Adams", "Musah"],
#         "arquero": "Steffen",
#         "datos": ["B", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     7: {
#         "nombre": "Gales",
#         "atq": ["Rodon", "Williams", "Davies"],
#         "dfc": ["Bale", "Moore", "James"],
#         "arquero": "Hennessey",
#         "datos": ["B", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     8: {
#         "nombre": "Argentina",
#         "atq": ["Messi", "De Paul", "Di Maria"], 
#         "dfc": ["Paredes", "Romero", "Otamendi"],
#         "arquero": "Dibu Martinez",
#         "datos": ["C", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     9: {
#        "nombre": "Arabia Saudita",
#        "atq": ["Al Faraj", "Al Muwallad", "Al Brikan"],
#        "dfc": ["Al-Ghannam", "Al Amri", "Al Bulaihi"],
#        "arquero": "Al Owais",
#        "datos": ["C", 0, 0],
#        "ranking": 4,
#        "mayorPosicion": "",
#     },
#     10: {
#         "nombre": "Mexico",
#         "atq": ["Lozano", "Corona", "Herrera"],
#         "dfc": ["Sanchez", "Montes", "Vasquez"],
#         "arquero": "Ochoa",
#         "datos": ["C", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     11: {
#         "nombre": "Polonia",
#         "atq": ["Lewandowski", "Moder", "Zielinksi"],
#         "dfc": ["Glik", "Cash", "Bednarek"],
#         "arquero": "Szczesny",
#         "datos": ["C", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     12: {
#         "nombre": "Francia",
#         "atq": ["Mpabbe", "Pogba","Griezmann"],
#         "dfc": ["Varane", "Benzema", "Kounde"],
#         "arquero": "Lloris",
#         "datos": ["D", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     13: {
#         "nombre": "Australia",
#         "atq": ["Rowles", "Boyle", "Behich"], 
#         "dfc": ["Mabil","Hrustic", "Wright"],
#         "arquero": "Ryan",
#         "datos": ["D", 0, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     14: {
#         "nombre": "Dinamarca",
#         "atq": ["Kjaer", "Poulsen", "Delaney"],
#         "dfc": ["Christensen", "Wass", "Skov Olsen"],
#         "arquero": "Schmeichel",
#         "datos": ["D", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     15: {
#         "nombre": "Tunez",
#         "atq": ["Jaziri", "Khazri", "Msakni"],
#         "dfc": ["Talbi", "Maaloul", "Ghandri"],
#         "arquero": "Ben Said",
#         "datos": ["D", 0, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     16: {
#         "nombre": "España",
#         "atq": ["Pedri", "Morata", "Dani Olmo"],
#         "dfc": ["Jordi Alba", "Laporte", "Eric Garcia"],
#         "arquero": "Unai Simon",
#         "datos": ["E", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     17: {
#         "nombre": "Costa Rica",
#         "atq": ["Oviedo", "Calvo", "Tejeda"],
#         "dfc": ["Torres" , "Campbell", "Fuller"],
#         "arquero": "Keylor Navas",
#         "datos": ["E", 0, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     18: {
#         "nombre": "Alemania",
#         "atq": ["T. Müller", "T. Werner", "Gnabry"],
#         "dfc": ["Sule", "Tisch", "Raum"],
#         "arquero": "Neuer",
#         "datos": ["E", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     19: {
#         "nombre": "Japon",
#         "atq": ["Minamino","Tanaka","J. Ito"],
#         "dfc": ["Tomiyasu", "Nagatomo", "Sakai"],
#         "arquero": "Gonda",
#         "datos": ["E", 0, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     20: {
#         "nombre": "Belgica",
#         "atq": ["Kevin De Bruyne", "Eden Hazard", "De Bruyne"],
#         "dfc": ["Denayer", "Vertoghen", "Witsel"],
#         "arquero": "Courtois",
#         "datos": ["F", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     21: {
#         "nombre": "Canada",
#         "atq": ["Larin", "Laryea", "Buchanan"],
#         "dfc": ["Miller", "S. Vitoria", "Johnston"],
#         "arquero": "Borjan",
#         "datos": ["F", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     22: {
#         "nombre": "Marruecos",
#         "atq": ["Louza","Amallah","El Kaabi"],
#         "dfc": ["Aguerd", "Masina", "Saiss"],
#         "arquero": "Bounou",
#         "datos": ["F", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     23: {
#         "nombre": "Croacia",
#         "atq": ["Kovacic", "Modric", "Juranovic"],
#         "dfc": ["Vlasic", "Perisic", "Sosa"],
#         "arquero": "Grbic",
#         "datos": ["F", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     24: {
#         "nombre": "Brasil",
#         "atq": ["Neymar Jr.", "Vini Jr.", "Paqueta"],
#         "dfc": ["Casemiro", "Danilo", "Thiago Silva"],
#         "arquero": "Alisson",   
#         "datos": ["G", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "",
#     },
#     25: {
#         "nombre": "Serbia",
#         "atq": ["Kostic", "Mitrovic", "Tadic"],
#         "dfc": ["Pavlovic", "Veljkovic", "Milenkovic"],
#         "arquero": "Rajkovic",
#         "datos": ["G", 0, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     26: {
#         "nombre": "Suiza",
#         "atq": ["Zakaria", "Vargas", "Okafor"],
#         "dfc": ["Mbabu", "Akanji", "Rodriguez"],
#         "arquero": "Sommer",
#         "datos": ["G", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     27: {
#         "nombre": "Camerun",
#         "atq": ["Fai","Ondoua", "Ngadeu"], 
#         "dfc": ["Aboubakar", "Choupo-Moting", "Castelleto"],
#         "arquero": "Onana",
#         "datos": ["G", 0, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
#     28: {
#         "nombre": "Portugal",
#         "atq": ["Ronaldo", "Jota", "Fernades"],
#         "dfc": ["Dias", "Pepe", "Cancelo"],
#         "arquero": "Costa",
#         "datos": ["H", 0, 0],
#         "ranking": 1,
#         "mayorPosicion": "", 
#     },    
#     29: {
#         "nombre": "Ghana",
#         "atq": ["Kudus", "Thomas Partey", "Fatawu"],
#         "dfc": ["Amartey","Baba", "Djiuku"],
#         "arquero": "Wollacott",
#         "datos": ["H", 7, 0],
#         "ranking": 4,
#         "mayorPosicion": "",
#     },
#     30: {
#         "nombre": "Uruguay",
#         "atq": ["Suarez", "Nuñez", "Valverde"],
#         "dfc": ["Gimenez", "Godin", "Araujo"],
#         "arquero": "Rochet",
#         "datos": ["H", 20, 0],
#         "ranking": 2,
#         "mayorPosicion": "",
#     },
#     31: {
#         "nombre": "Corea del Sur",
#         "atq": ["Min-Jae", "Jin-Su", "Hee-Chan"],
#         "dfc": ["Jae-Sung", "Young-Gwon", "Lee young"],
#         "arquero": "Seung-Gyu",
#         "datos": ["H", 6, 0],
#         "ranking": 3,
#         "mayorPosicion": "",
#     },
# }

# clasificados2(paises)