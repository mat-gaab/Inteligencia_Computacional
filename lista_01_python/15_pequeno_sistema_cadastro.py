def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return nome, idade

def mostrar_boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a) ao sistema.")

def mostrar_menu():
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar mensagem de boas-vindas")
    print("3 - Sair")

nome = ""

opcao = ""

while opcao != "3":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome, idade = cadastrar_pessoa()
        print("Pessoa cadastrada com sucesso!")
    elif opcao == "2":
        if nome != "":
            mostrar_boas_vindas(nome)
        else:
            print("Nenhuma pessoa cadastrada.")
    elif opcao == "3":
        print("Programa encerrado.")
    else:
        print("Opção inválida!")
