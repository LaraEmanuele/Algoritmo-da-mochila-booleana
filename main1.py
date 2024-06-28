import os
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
        return lista, beneficio
    else:#Caso de erro na abertura do arquivo
        print("Erro ao abrir o arquivo!!!")
        arquivo.close() #Realiza o fechamento do arquivo
        return -1

def leArquivoTeste(x, y):
    #Obtem o diretório dos dados
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "low-dimensional",
                   f"f4_l-d_kp_{x}_{y}"), "r")
    
    lista = [] #Armazena os valores e os pesos
    
    if arquivo: #Verifica se o arquivo foi aberto corretamente
        for linha in arquivo: #Realiza a leitura do arquivo linha por linha
            dados = linha.split() #Separa os dados por meio de " " e gera uma lista dos elementos
            valores = [int(valor) for valor in dados] #Para cada elemento obtido converte a string em inteiro
            lista.append(valores)
        arquivo.close() #Realiza o fechamento do arquivo
        beneficio = lista[0][1]
        return lista, beneficio
    else:#Caso de erro na abertura do arquivo
        print("Erro ao abrir o arquivo!!!")
        arquivo.close() #Realiza o fechamento do arquivo
        return -1

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
            print(f"j: {j}")
            if lista[i][1] > j:
                listaResp [i][j] = listaResp[i-1][j]
            else:
                aux = listaResp[i-1][(j-lista[i][1])]
                listaResp [i][j] =  max(listaResp[i-1][j], (lista[i][0] + aux))
    return listaResp

#Processo de leitura e armazenamento dos dados



lista_1_100, beneficio_1_100 = leArquivo(1, 100)
listaResp_1_100 = respostaDinamica (lista_1_100)
lista_1_200, beneficio_1_200 = leArquivo(1, 200)
listaResp_1_200 = respostaDinamica (lista_1_200)
lista_1_500, beneficio_1_500 = leArquivo(1, 500)
listaResp_1_500 = respostaDinamica (lista_1_500)

lista_1_1000, beneficio_1_1000 = leArquivo(1, 1000)
listaResp_1_1000 = respostaDinamica (lista_1_1000)
lista_1_2000, beneficio_1_2000 = leArquivo(1, 2000)
listaResp_1_2000 = respostaDinamica (lista_1_2000)
lista_1_5000, beneficio_1_5000 = leArquivo(1, 5000)
listaResp_1_5000 = respostaDinamica (lista_1_5000)
lista_1_10000, beneficio_1_10000 = leArquivo(1, 10000)
listaResp_1_10000 = respostaDinamica (lista_1_10000)


lista_2_100, beneficio_2_100 = leArquivo(2, 100)
listaResp_2_100 = respostaDinamica (lista_2_100)
lista_2_200, beneficio_2_200 = leArquivo(2, 200)
listaResp_2_200 = respostaDinamica (lista_2_200)
lista_2_500, beneficio_2_500 = leArquivo(2, 500)
listaResp_2_500 = respostaDinamica (lista_2_500)

lista_2_1000, beneficio_2_1000 = leArquivo(2, 1000)
listaResp_2_1000 = respostaDinamica (lista_2_1000)
lista_2_2000, beneficio_2_2000 = leArquivo(2, 2000)
listaResp_2_2000 = respostaDinamica (lista_2_2000)
lista_2_5000, beneficio_2_5000 = leArquivo(2, 5000)
listaResp_2_5000 = respostaDinamica (lista_2_5000)
lista_2_10000, beneficio_2_10000 = leArquivo(2, 10000)
listaResp_2_10000 = respostaDinamica (lista_2_10000)

lista_3_100, beneficio_3_100 = leArquivo(3, 100)
listaResp_3_100 = respostaDinamica (lista_3_100)
lista_3_200, beneficio_3_200 = leArquivo(3, 200)
listaResp_3_200 = respostaDinamica (lista_3_200)
lista_3_500, beneficio_3_500 = leArquivo(3, 500)
listaResp_3_500 = respostaDinamica (lista_3_500)

lista_3_1000, beneficio_3_1000 = leArquivo(3, 1000)
listaResp_3_1000 = respostaDinamica (lista_3_1000)
lista_3_2000, beneficio_3_2000 = leArquivo(3, 2000)
listaResp_3_2000 = respostaDinamica (lista_3_2000)
lista_3_5000, beneficio_3_5000 = leArquivo(3, 5000)
listaResp_3_5000 = respostaDinamica (lista_3_5000)
lista_3_10000, beneficio_3_10000 = leArquivo(3, 10000)
listaResp_3_10000 = respostaDinamica (lista_3_10000)

"""

