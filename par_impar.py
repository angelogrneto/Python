numero = int(input('Digite um numero: '))
result = numero % 2

if result == 1:
    print('O numero {} é impar'.format(numero, result))
else:
    print('O numero {} é par'.format(numero, result))