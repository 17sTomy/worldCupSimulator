import paises
import funciones

SELECCIONES = paises.paises
fecha = 1
seleccion = None
proximoRival = None

# grupoH = funciones.crearGrupo(SELECCIONES, "H")
# funciones.imprimirGrupo(grupoH)

grupos = funciones.crearGrupos(SELECCIONES)
funciones.updateTablas(SELECCIONES, grupos)


funciones.imprimirGrupo(grupos)