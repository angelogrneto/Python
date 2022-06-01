valor = float(input('Digite o valor do pagamento: '))
print(''' SELECINE A FORMA DE PAGAMENTO:
[1] À VISTA EM DINHEIRO
[2] À VISTA NO CARTÃO  
[3] 2X NO CARTÃO
[4] 3X NO CARTÃO''' )
opcao = int(input('Qual Opção?'))



if opcao == 1:
    real = valor-(valor*10/100)
    print('Você vai pagar {}'.format(real))
elif opcao == 2:
    real = valor-(valor*5/100)
    print('Você vai pagar {}'.format(real))
elif opcao == 3:
    real = valor
    print('Você vai pagar {}'.format(real))
elif opcao == 4:
    real = valor+(valor*20/100)
    print('Você vai pagar {}'.format(real))
else:
    print('Digite uma opção valida')

    