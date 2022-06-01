salario = float(input('Qual o seu salario: '))
aumento = float(input('Aumento salario %: '))
#salario_atual = salario+(salario*aumento/100)
#print(salario_atual)


print('Seu salario atual é de R${}, com o aumento de %{:.0f} seu salario atual é de: R${}'.format(salario, aumento,salario+(salario*aumento/100) ))