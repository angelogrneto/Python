
#ADIVINHAR QUAL NUMERO O COMPUTADOR ESTA PENSANDO

import random


escolhido = random.randint(0,11) #SORTEIA UM NUMERO DE 1 A 10
#print('O aluno escolhido é: {}'.format(escolhido))
 
numero = int(input('Qual numero o computador esta pensando? '))
soma = 1 
while numero != escolhido:
    
    numero = int(input('Qual numero o computador esta pensando? '))
    soma = soma +1
    

print('Parabens, voce acertou! Voce tentou {}x até acertar. O computador pensou o numero: {}'.format(soma, escolhido))


