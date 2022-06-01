

lista = []
continuar = ''
while continuar !=  'N':
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar [S/N] ?').strip()
    
   


lista.sort()
print(lista)
