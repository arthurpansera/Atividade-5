#Atividade 5: Exercícios (Matrizes)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

tabuleiro=[[0,0,0],
         [0,0,0],
         [0,0,0]]

def jogo_da_velha():
    turno = 0
    while ganhou() == 0:
        print("\n")
        print(30*"-")
        print(f"\nVez do jogador {turno % 2 + 1}")
        marcar()
        linha  = int(input("\nLinha: "))
        coluna = int(input("Coluna: "))
        if tabuleiro[linha - 1][coluna - 1] == 0:
            if (turno % 2 + 1) == 1:
                tabuleiro[linha - 1][coluna - 1] = 1
            else:
                tabuleiro[linha - 1][coluna - 1] = -1
        else:
            print("Nao está vazio")
            turno -=1
        if ganhou():
            print(f"Jogador {turno % 2 + 1} ganhou após {turno + 1} rodadas!")
        turno +=1
    
def ganhou():
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == 3 or soma == -3:
            return 1
    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma == 3 or soma == -3:
            return 1
    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1
    return 0

def marcar():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" X ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end=' ')
        print()

def menu():
    while True:
        print("\n----------JOGO DA VELHA----------")
        print("0. Sair\n1. Jogar\n")
        escolha = int(input("Escolha uma das opções: "))
        if escolha == 1:
            jogo_da_velha()
        else:
            print("Saindo...")
          
menu()