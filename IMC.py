altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / (altura**2)

print(imc)


if imc < 18.5:
    print('Seu IMC é de {}, voce esta abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <=25:
    print('Seu IMC é de {}, voce esta dentro do peso ideal'.format(imc))
elif imc > 25 and imc <=30:
    print('Seu IMC é de {}, você esta com sobrepeso'.format(imc))
elif imc >30 and imc <=40:
    print('Seu IMC é {}, você esta com obesidade'.format(imc))
else:
    print('Seu IMC é {}, você esta com obesidade morbida'.format(imc))





