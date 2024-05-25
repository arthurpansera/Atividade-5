#Atividade 5: Exercícios (Matrizes)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

import random

def gerar_matriz(num_linhas,num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento_sorteado = random.randint(1,20)
            linha.append(elemento_sorteado)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def soma_coluna(matriz,coluna):
    soma_num_coluna = 0
    while coluna > colunas and coluna <= 0:
        coluna = int(input("Coluna não existe! Escolha uma coluna da matriz para somar os elementos: "))
    for linha in matriz:
        soma_num_coluna += linha[coluna]
    return soma_num_coluna

linhas = int(input("Informe o número de linhas que a matriz terá: "))
colunas = int(input("Informe o número de colunas que a matriz terá: "))
matriz = gerar_matriz(linhas,colunas)
imprimir_matriz(matriz)
coluna = int(input("Escolha uma coluna da matriz para somar os elementos: "))
print(f"A soma dos números da {coluna}º coluna é: {soma_coluna(matriz,coluna-1)}")