import os

def calculaBeneficio (lista, listaBeneficio):
    beneficio = 0
    for i in range(len(listaBeneficio)):
        if listaBeneficio[i] != 0:
            beneficio = beneficio + (lista[i][0] * lista[i][1])

    return beneficio

def leArquivo(x, y):
    #Obtem o diretório dos dados
    diretorio_atual = os.getcwd()
    arquivo = open(os.path.join(diretorio_atual, "instances_01_KP",
                   "large_scale", f"knapPI_{x}_{y}_1000_1"), "r")
    
    lista = [] #Armazena os valores e os pesos
    #listaBeneficio = [] #Armazena o valor do melhor benefício
    count = 0
    
    if arquivo: #Verifica se o arquivo foi aberto corretamente
        for linha in arquivo: #Realiza a leitura do arquivo linha por linha
            dados = linha.split() #Separa os dados por meio de " " e gera uma lista dos elementos
            valores = [int(valor) for valor in dados] #Para cada elemento obtido converte a string em inteiro
            count = count + 1
            if count == (y+2): #Verifica se essa é a última linha do arquivo
                #listaBeneficio.append(valores)
                beneficio = calculaBeneficio (lista, valores)
            else:
                lista.append(valores)
        arquivo.close() #Realiza o fechamento do arquivo
        return lista, beneficio
    else:#Caso de erro na abertura do arquivo
        print("Erro ao abrir o arquivo!!!")
        arquivo.close() #Realiza o fechamento do arquivo
        return -1

#Processo de leitura e armazenamento dos dados
lista_1_100, beneficio_1_100 = leArquivo(1, 100)
lista_1_200, beneficio_1_200 = leArquivo(1, 200)
lista_1_500, beneficio_1_500 = leArquivo(1, 500)

lista_1_1000, beneficio_1_1000 = leArquivo(1, 1000)
lista_1_1000, beneficio_1_1000 = leArquivo(1, 2000)
lista_1_5000, beneficio_1_5000 = leArquivo(1, 5000)
lista_1_1000, beneficio_1_1000 = leArquivo(1, 10000)

lista_2_100, beneficio_2_100 = leArquivo(2, 100)
lista_2_200, beneficio_2_200 = leArquivo(2, 200)
lista_2_500, beneficio_2_500 = leArquivo(2, 500)

lista_2_1000, beneficio_2_1000 = leArquivo(2, 1000)
lista_2_1000, beneficio_2_1000 = leArquivo(2, 2000)
lista_2_5000, beneficio_2_5000 = leArquivo(2, 5000)
lista_2_1000, beneficio_2_1000 = leArquivo(2, 10000)

lista_3_100, beneficio_3_100 = leArquivo(3, 100)
lista_3_200, beneficio_3_200 = leArquivo(3, 200)
lista_3_500, beneficio_3_500 = leArquivo(3, 500)

lista_3_1000, beneficio_3_1000 = leArquivo(3, 1000)
lista_3_1000, beneficio_3_1000 = leArquivo(3, 2000)
lista_3_5000, beneficio_3_5000 = leArquivo(3, 5000)
lista_3_1000, beneficio_3_1000 = leArquivo(3, 10000)



