#Atividade 5: Exercícios (Matrizes)
#Aluno: Arthur Rodrigues Pansera
#Turma: C

def cadastrar_pessoa():
    nome = input("Informe o nome da pessoa: ")
    cpf = input("Informe o CPF da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    renda_mensal = float(input("Informe a renda mensal da pessoa: "))
    return [nome, cpf, idade, renda_mensal]

def calcular_idade(pessoas):
    idade_total = 0
    for pessoa in pessoas:
        idade_total += pessoa[2]
    media_idade = idade_total/len(pessoas)
    return media_idade

def calcular_renda(pessoas):
    renda_total = 0
    for pessoa in pessoas:
        renda_total += pessoa[3]
    media_renda = renda_total/len(pessoas)
    return media_renda

def cadastro():
    pessoas = []
    while True:
        pessoa = cadastrar_pessoa()
        pessoas.append(pessoa)
        print(pessoas)
        outro_cadastro = input("Deseja cadastrar outra pessoa? (s/n): ")
        if outro_cadastro == "s":
            continue
        else:
            break
    for pessoa in pessoas:
        print(f"\nNome: {pessoa[0]}")
        print(f"CPF: {pessoa[1]}")
        print(f"Idade: {pessoa[2]}")
        print(f"Renda mensal: R${pessoa[3]}")
    print(f"\nA média de idade das pessoas cadastradas é: {calcular_idade(pessoas)}")
    print(f"A média da renda das pessoas cadastradas é: {calcular_renda(pessoas)}")

cadastro()