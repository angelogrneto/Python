velocidade = int(input('Qual sua velocidade? '))

if velocidade <=80:
    print('Sua velocidade é de {}, voce esta dentro do limite'.format(velocidade))
else:
    print('Sua velocidade é de {}, voce sera multado!'.format(velocidade))