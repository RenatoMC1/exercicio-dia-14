média = 0
contador = 0

while contador >= 0:
    nota = float(input("Digite a nota e caso deseje a média das notas digite [0]: "))
    if nota == 0:
        break

    contador = contador + 1
    média += nota / 2

print("a média é: ", média)