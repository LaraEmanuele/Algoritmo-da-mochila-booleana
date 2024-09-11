import os
from timeit import timeit
from SolucaoDinamica import respostaDinamica
import SolucaoGulosa as sg
import PreparoLista as pl


"""
Como a primeira linha do arquivo informa a quantidade de itens e a capacidade da mochila
a lista de itens levados no caso ótimo encontra-se 2 linha a frente
e deve-se ter o cuidado de não utilizar a primeira linha como um item!!!
"""

def calculaBeneficio (lista, listaBeneficio):
    beneficio = 0
    for i in range(len(listaBeneficio[0])):
        beneficio = beneficio + (listaBeneficio[0][i] * lista[i+1][0])
    return beneficio

def leArquivo(x, y):
    #Obtem o diretório dos dados
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "instances_01_KP",
                   "large_scale", f"knapPI_{x}_{y}_1000_1"), "r")
    
    lista = [] #Armazena os valores e os pesos
    listaBeneficio = [] #Armazena o valor do melhor benefício
    count = 0
    
    if arquivo: #Verifica se o arquivo foi aberto corretamente
        for linha in arquivo: #Realiza a leitura do arquivo linha por linha
            dados = linha.split() #Separa os dados por meio de " " e gera uma lista dos elementos
            valores = [int(valor) for valor in dados] #Para cada elemento obtido converte a string em inteiro
            count = count + 1
            if count == (y+2): #Verifica se essa é a última linha do arquivo
                listaBeneficio.append(valores)
                beneficio = calculaBeneficio (lista, listaBeneficio)
            else:
                lista.append(valores)
        arquivo.close() #Realiza o fechamento do arquivo
        return lista
    else:#Caso de erro na abertura do arquivo
        print("Erro ao abrir o arquivo!!!")
        arquivo.close() #Realiza o fechamento do arquivo
        return -1


def escritaResultados (x, y):
    lista = leArquivo(x, y)
    diretorio_atual = os.getcwd()
    qtdItens, capacidadeMax, pesos, beneficios = pl.divisaoLista(lista)
    
    #with  open(os.path.join(diretorio_atual, "Resultados", f"Tipo{x}", f"Dinamica"), "a") as arq:
        #beneficio = respostaDinamica (lista)
        #tempo = timeit(f'respostaDinamica ({lista})', number=100,globals=globals())
        #arq.write(f"{y} , {str(beneficio[-1][-1])}, {str (tempo)}\n")
    
    with  open(os.path.join(diretorio_atual, "Resultados", f"Tipo{x}", f"Gulosa1"), "a") as arq:
        beneficio = sg.gulosoMenorPesoMelhorado (qtdItens, capacidadeMax, beneficios, pesos)
        tempo = timeit(f'sg.gulosoMenorPesoMelhorado ({qtdItens}, {capacidadeMax}, {beneficios}, {pesos})', number=100,globals=globals())
        arq.write(f"{y} , {str(beneficio)}, {str (tempo)}\n")

    with  open(os.path.join(diretorio_atual, "Resultados", f"Tipo{x}", f"Gulosa2"), "a") as arq:
        listaGeral = pl.divisaoBeneficioCusto (qtdItens, pesos, beneficios)
        beneficio = sg.gulosoBeneficioCustoMelhorado (qtdItens, capacidadeMax, listaGeral)
        tempo = timeit(f'sg.gulosoBeneficioCustoMelhorado ({qtdItens}, {capacidadeMax}, {listaGeral})', number=100,globals=globals())
        arq.write(f"{y} , {str(beneficio)}, {str (tempo)}\n")
    
    