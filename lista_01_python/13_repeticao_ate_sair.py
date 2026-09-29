opcao = ""

while opcao != "0":
    print("1 - Dizer Olá")
    print("2 - Mostrar mensagem")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        print("Bem-vindo ao sistema!")
    elif opcao == "0":
        print("Programa encerrado.")
    else:
        print("Opção inválida!")
