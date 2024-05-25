#Atividade 5: Exercícios (Matrizes)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

import random

def gerar_matriz(num_linhas,num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            if i < j:
                elemento_sorteado = 2*i + 7*j + 2
            elif i == j:
                elemento_sorteado = 3*i**2 + 1
            else:
                elemento_sorteado = 4*i**3 + 5*j**2 + 1
            linha.append(elemento_sorteado)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz = gerar_matriz(10,10)
imprimir_matriz(matriz)