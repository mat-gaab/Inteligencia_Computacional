print("1 - Consultar horário de atendimento")
print("2 - Falar com atendente")
print("3 - Encerrar")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Horário de atendimento: 08:00 às 18:00.")
elif opcao == "2":
    print("Você será encaminhado para um atendente.")
elif opcao == "3":
    print("Atendimento encerrado.")
else:
    print("Opção inválida!")
