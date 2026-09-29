def verificar_idade(idade):
    if idade < 18:
        print("Menor de idade.")
    else:
        print("Maior de idade.")

idade = int(input("Digite sua idade: "))
verificar_idade(idade)
