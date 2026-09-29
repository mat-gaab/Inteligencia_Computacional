produto = input("Digite o nome do produto: ")
estoque = int(input("Digite a quantidade disponível: "))
quantidade = int(input("Digite a quantidade que deseja comprar: "))

print("Produto:", produto)
print("Estoque:", estoque)
print("Quantidade desejada:", quantidade)

if quantidade <= estoque:
    print("Compra autorizada!")
else:
    print("Estoque insuficiente!")
