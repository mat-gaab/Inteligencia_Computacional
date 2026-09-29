senha_correta = "python123"
tentativas = 0
acesso = False

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso autorizado!")
        acesso = True
        break

    print("Senha incorreta!")
    tentativas += 1

if acesso == False:
    print("Número máximo de tentativas atingido.")
    print("Acesso bloqueado.")
