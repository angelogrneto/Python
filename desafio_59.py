#PROGRAMA QUE LE DOIS VALORES, MOSTRA SOMA, MULTIPLCA, MAIOR VALOR, NOVOS NUMEROS E SAI DO PROGRAMA


opcao = 0
while opcao != 5:

    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    soma = 0
    multiplicar = 0
    maior = 0
    
    
    print(''' SELECIONE  O QUE DESEJA FAZESR
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual Opção?'))




    if opcao == 1:
        soma = num1 + num2
        print("O Valor da soma é: {}".format(soma))
    if opcao == 2:
        multiplicar = (num1 * num2)
        print("O Valor da multplicação é: {}".format(multiplicar))
    if opcao == 3:
        if num1 > num2:
            print('O numero {} é maior que o numero {} '.format(num1,num2))
        elif num2 > num1:
            print('O numero {} é maior que o numero6 {} '.format(num2,num1))
        else:
            print('Os numeros são iguais')
    if opcao == 5:
        print('Saindo........')
