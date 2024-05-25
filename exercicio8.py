#Atividade 5: Exercícios (Matrizes)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            print(f"{elemento}|")
        print("\n")
        print("-"*len(linha))