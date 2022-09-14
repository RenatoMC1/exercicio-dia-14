soma = 0
média = 0

for contador in range(1,6):
    nota = int(input(f"digite a {contador} nota: "))
    soma = soma + nota
    média = soma/contador

print(f"a média é: ", média)