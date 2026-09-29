nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota final: "))

if nota >= 7:
    situacao = "Aprovado"
elif nota >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Nome:", nome)
print("Nota:", nota)
print("Situação:", situacao)
