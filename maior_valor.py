num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print('O maior numero é: {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior numero é: {}'.format(num2))
else:
    print('O maior numero é {}'.format(num3))