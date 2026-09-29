valor = float(input("Digite o valor da compra: "))

if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    recebeu_desconto = "Sim"
else:
    valor_final = valor
    recebeu_desconto = "Não"

print(f"Valor da compra: R$ {valor:.2f}")
print("Recebeu desconto:", recebeu_desconto)
print(f"Valor final a pagar: R$ {valor_final:.2f}")
