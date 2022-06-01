valor = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o desconto: '))
real = valor-(valor*desconto/100)
print(real)


print('O valor do produto é R$ {:.1f}, \nCom desconto de %{:.1f} o produto fica: R${:.1f}'.format(valor, desconto, valor-(valor*desconto/100)))