import copy

def gulosoMenorPeso (listaOriginal):
    lista = copy.deepcopy(listaOriginal)
    qtdItens = lista[0][0] #Constante que indica o número de itens na mochila
    w = lista[0][1]#Constante que indica capacidade máxima na mochila
    aux = [1001, 1001, 1001]
    capacidadeRestante = w
    beneficio = 0
    limite = 0 # Se 1 não a itens para inserir com a capacidade restante
    listaResult = []

    while w != 0 and qtdItens > -1 and limite != 1:
        for i in range (1, len(lista)):
            if capacidadeRestante >= lista[i][1] and lista[i][1] < aux[1]:
                aux = [lista[i][0], lista[i][1], i]
            elif capacidadeRestante >= lista[i][1] and lista[i][1] == aux[1]:
                if lista[i][0] > aux[0]:
                    aux = [lista[i][0], lista[i][1], i]
        if aux != [1001, 1001, 1001]:
            listaResult.append(aux)
            beneficio = beneficio + aux[0]
            capacidadeRestante = capacidadeRestante - aux[1]
            del lista [aux[2]]
            aux = [1001, 1001, 1001]
        else:
            limite = 1

    return listaResult, beneficio

def gulosoBeneficioCusto (listaOriginal):
    lista = copy.deepcopy(listaOriginal)
    qtdItens = lista[0][0] #Constante que indica o número de itens na mochila
    w = lista[0][1]#Constante que indica capacidade máxima na mochila
    aux = [-1, -1, -1]
    capacidadeRestante = w
    beneficio = 0
    limite = 0 # Se 1 não a itens para inserir com a capacidade restante
    listaResult = []

    while w != 0 and qtdItens > -1 and limite != 1:
        for i in range (1, len(lista)):
            if capacidadeRestante >= lista[i][1] and (lista[i][0]/lista[i][1]) > (aux[0]/aux[1]):
                aux = [lista[i][0], lista[i][1], i]
            elif capacidadeRestante >= lista[i][1] and (lista[i][0]/lista[i][1]) == (aux[0]/aux[1]):
                if lista[i][0] > aux[0]:
                    aux = [lista[i][0], lista[i][1], i]
        if aux != [-1, -1, -1]:
            listaResult.append(aux)
            beneficio = beneficio + aux[0]
            capacidadeRestante = capacidadeRestante - aux[1]
            del lista [aux[2]]
            aux = [-1, -1, -1]
        else:
            limite = 1
            
    return listaResult, beneficio