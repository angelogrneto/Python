dias = float(input('Quantos dias você utilizou o carro? '))
km = float(input('Quando KM voce andou com o carro? '))

#aluguel = 60 * dias + km * 0.15

#print(aluguel)

print('Voce utilizou o carro por {} dias, e andou um total de {} Km. Seu aluguel fico em R${}'.format(dias, km, (60 * dias + km * 0.15) ))