import math

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = nota1 + nota2
total = media/2

print('Sua média é {:.1f}'.format(media, math.ceil(total)))

#match.ceil arredonda pra cima

