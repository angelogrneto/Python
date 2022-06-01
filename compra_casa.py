valor_casa = float(input('Qual o valor do imovel? '))
salario = float(input('Qual o seu salario? '))
financiamento = float(input('Em quantos anos voce vai pagar? '))

fin_total = financiamento / 12
prestacao = valor_casa / fin_total

aprovacao = (salario*100) /  30 

print(aprovacao)

if prestacao > (salario*100) /  30:
    print('Financiamento negado, prestação de R${} é maior que 30 por cento do seu salario'.format(prestacao))
else:
    print('Financiamento aprovado')


