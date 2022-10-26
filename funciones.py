def crearGrupo(grupo):
    matriz = []
    for f in range(5):
        matriz.append([])
        if f == 0:
            matriz[f].append(f"Grupo {grupo}")
            matriz[f].append("Puntos")
            matriz[f].append("Goles")
        else:
            matriz[f].append("Argentina")
            matriz[f].append(f"   {0}")
            matriz[f].append(f"          {0}")

    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

crearGrupo("H")