nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Sua média é {:.1f}, você esta aprovado'.format(media))
elif media < 5:
    print('Sua média é {:.1f}, você esta de reprovado'.format(media))
else:
    print('Sua média é {:.1f}, você esta de recuperação'.format(media))

