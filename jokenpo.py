from random import choice

escolha, joken = str(input('escolha pedra, papel ou tesoura: ')).strip(), \
                ('papel', 'pedra', 'tesoura')
random = choice(joken)
print('{} x \033[1;4m{}'.format(random.upper(), escolha.upper()))

if escolha == random:
    print('\033[1;3;32mdeu empate')
elif random == 'papel' and \
        escolha == 'pedra' or \
        random == 'tesoura' and \
        escolha == 'papel':
    print('\033[1;3;31mvocê perdeu!')
elif random == 'pedra' and \
        escolha == 'tesoura':
    print('\033[1;3;31mvocê perdeu.')
else:
    print('\033[1;3;34mvocê ganhou!!!')