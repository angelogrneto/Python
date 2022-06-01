from datetime import date
data_atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))

idade = data_atual - ano

if idade == 18:
    print('Voce tem {} anos e deve se alistar!'.format(idade))
elif idade <18:
    print('Voce ainda é muito novo!')    
else:
    print('Voce tem {} anos, ja passou da idade de se alistar'.format(idade))




