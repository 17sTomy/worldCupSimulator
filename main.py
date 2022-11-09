import paises
import funciones
import eliminatorias
import faseGrupos

SELECCIONES = paises.paises
fecha = 1
miEquipo = 8
proximoRival = None

if __name__ == '__main__':
    pass
funciones.ejectProgressBar()
tabla_general = faseGrupos.simuladorFaseGrupos(SELECCIONES, miEquipo)
seleccionesClasificadas = funciones.clasificados(tabla_general)
eliminatorias.eliminaciones(SELECCIONES, seleccionesClasificadas, miEquipo, 8)

