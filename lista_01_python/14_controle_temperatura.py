def classificar_temperatura(temperatura):
    if temperatura < 18:
        print("Está frio.")
    elif temperatura <= 28:
        print("Temperatura agradável.")
    else:
        print("Está quente.")

temperatura = float(input("Digite a temperatura atual: "))
classificar_temperatura(temperatura)
