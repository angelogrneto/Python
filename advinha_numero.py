from random import randint
from time import sleep

print('Processando...')
sleep = 3

computador = randint(0,10)
jogador = int(input('Que numero estou pensando? '))




if jogador == computador:
    print('Voce acertou!'.format(computador))
else:
    print('Voce errou, eu pensei o numero {}'.format(computador))



#print('Pensei no numero: {}'.format(computador))