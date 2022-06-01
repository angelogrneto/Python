#sorteia uma lista em sequencia para apresentar trabalho

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('O aluno escolhido é: {}'.format(lista))
