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

def soma_linha(matriz,linha):
    soma_num_linha = 0
    for elemento_sorteado in matriz[linha]:
        soma_num_linha += elemento_sorteado
    return soma_num_linha

linhas = int(input("Informe o número de linhas que a matriz terá: "))
colunas = int(input("Informe o número de colunas que a matriz terá: "))
matriz = gerar_matriz(linhas,colunas)
imprimir_matriz(matriz)
linha = int(input("Escolha uma linha da matriz para somar os elementos: "))
while linha > linhas or linha <= 0:
        linha = int(input("Linha inexistente! Escolha uma linha da matriz para somar os elementos: "))
print(f"A soma dos números da {linha}º linha é: {soma_linha(matriz,linha-1)}")