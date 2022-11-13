import paises
import funciones
import eliminatorias
import faseGrupos
import adm_archivos
 
SELECCIONES = paises.paises

if __name__ == '__main__':
    funciones.ejectProgressBar()
    MUNDIAL, USUARIO, MIEQUIPO = adm_archivos.partida(SELECCIONES)
    if MUNDIAL == SELECCIONES:
        tabla_general = faseGrupos.simuladorFaseGrupos(SELECCIONES, MIEQUIPO)
        desea_seguir = input("¿Desea continuar la partida? Presione cualquier tecla para SI, si usted quiere guardar la partida presione ENTER: ")
        if desea_seguir:
            seleccionesClasificadas = funciones.clasificados(tabla_general)
            eliminatorias.eliminaciones(SELECCIONES, seleccionesClasificadas, MIEQUIPO, 8)
            adm_archivos.cargar_historial(SELECCIONES, USUARIO, MIEQUIPO)
            adm_archivos.mostrar_historial()
        else:
            adm_archivos.cargar_progreso(SELECCIONES, USUARIO, MIEQUIPO)
    else:
        seleccionesClasificadas = funciones.clasificados2(MUNDIAL)
        eliminatorias.eliminaciones(SELECCIONES, seleccionesClasificadas, MIEQUIPO, 8)
        adm_archivos.cargar_historial(MUNDIAL, USUARIO, MIEQUIPO)
        adm_archivos.mostrar_historial()


