from datetime import date
data = date.today().year

nasc = int(input('Digite seu ano de nascimento: '))

idade = data - nasc

if idade <= 9:
    print('Voce tem {} anos, voce é MIRIM'.format(idade))
elif idade <=14:
    print('Voce tem {} anos, voce é INFANTIL'.format(idade))
elif idade <=19:
    print('Voce tem {} anos, voce é JUNIOR'.format(idade))
elif idade <=25:
    print('Voce tem {} anos, voce é SÊNIOR'.format(idade))
else:
    print('Voce tem {} anos, voce é MASTER'.format(idade))