
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input('Digite um numero: '))
    soma += num
    quant += +1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num
    resp = str(input('Desja continuar? [S/N]')).upper().strip()[0]

media = soma / quant
print('Voce digitou {} numeros e a média é de {} '.format(quant, media))
print('Acabou')
print('O maior numero é {}  e o menor numero é {}'.format(maior, menor))