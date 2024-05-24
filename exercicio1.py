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

linhas = int(input("Informe o número de linhas que a matriz terá: "))
colunas = int(input("Informe o número de colunas que a matriz terá: "))
matriz = gerar_matriz(linhas,colunas)