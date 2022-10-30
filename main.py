import paises
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