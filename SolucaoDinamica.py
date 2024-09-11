def respostaDinamica (lista):
    listaResp = []
    W = lista[0][1]
    qtdItens = lista[0][0]
    auxLista = []
    aux = -1

    for i in range(qtdItens+1):
        listaResp.append([])
        for j in range(W+1):
            listaResp[i].append(0)

    for i in range (1, qtdItens+1): 
        for j in range (1, W+1):
            if lista[i][1] > j:
                listaResp [i][j] = listaResp[i-1][j]
            else:
                aux = listaResp[i-1][(j-lista[i][1])]
                listaResp [i][j] =  max(listaResp[i-1][j], (lista[i][0] + aux))

    
    return listaResp

