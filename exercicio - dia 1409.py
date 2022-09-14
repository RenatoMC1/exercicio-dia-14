contador = 1
maior = 0
menor = 0

while contador <= 10:
    n1 = int(input(f"Digite {contador} número: "))
    if contador == 1:
        maior = n1
        menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1

    contador = contador + 1

print(f"o maior é {maior} e o menor é {menor}")