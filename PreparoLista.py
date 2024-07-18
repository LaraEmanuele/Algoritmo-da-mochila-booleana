import heapq
import copy
def divisaoLista (lista):
    pesos = []
    beneficios = []
    qtdItens = lista[0][0]
    capacidadeMax = lista[0][1]
    del lista [0]

    for i in range (len(lista)):
        pesos.append([lista[i][1], i])
        beneficios.append(lista[i][0])

    return qtdItens, capacidadeMax, pesos, beneficios

def divisaoBeneficioCusto (qtdItens, pesos, beneficios):
    pesosAtualizado = []

    for i in range(qtdItens):
        pesosAtualizado.append([(beneficios[pesos[i][1]]/pesos[i][0]), pesos[i][0], beneficios[pesos[i][1]]])
    return pesosAtualizado

def heapSort (pesos):
    listaOrdenada = []
    pesosCopy = copy.deepcopy(pesos)
    heapq.heapify(pesosCopy)
    
    while len(pesosCopy) > 0:
        maior = heapq.heappop(pesosCopy)
        listaOrdenada.append(maior)
    return listaOrdenada