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

def soma_pares_matriz(matriz):
    soma_pares = 0
    for elemento_sorteado in matriz:
        if elemento_sorteado % 2 == 0:
            soma_pares += elemento_sorteado
    return soma_pares

linhas = int(input("Informe o número de linhas que a matriz terá: "))
colunas = int(input("Informe o número de colunas que a matriz terá: "))
matriz = gerar_matriz(linhas,colunas)
imprimir_matriz(matriz)
soma_pares_matriz(matriz)