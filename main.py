import paises

SELECCIONES = paises.paises

for pais in SELECCIONES:
    print(pais)
    print(SELECCIONES[pais])
    print(SELECCIONES[pais]["jugadores"])
    print(SELECCIONES[pais]["jugadores"][0])
    print(SELECCIONES[pais]["jugadores"])
    print()
