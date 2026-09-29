def calcular_desconto(valor):
    if valor > 100:
        return valor - (valor * 0.10)
    return valor

valor = float(input("Digite o valor da compra: "))
valor_final = calcular_desconto(valor)

print(f"Valor final: R$ {valor_final:.2f}")
