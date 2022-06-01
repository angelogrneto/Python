maior = 0
menor = 0

for p in range(0,5):
    peso = float(input("digite o peso da {} pessoa: ".format(p)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é: {}'.format(menor))