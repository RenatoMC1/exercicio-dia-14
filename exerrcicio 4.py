soma = 0
par = 0
impar = 0

for contador in range(1,11):
    numero = int(input(f"digite o {contador}ª número: "))
    soma = soma + numero
    if numero %2 == 0:
        par = par + numero
    else:
        impar = impar + numero

print(f"a soma total é {soma}, sendo:")
print(f"a soma dos números pares: ", par)
print(f"a soma dos números ímpares: ", impar)