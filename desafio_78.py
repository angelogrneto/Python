max_valor = None
min_valor = None


valor = []
for n in range(0,5):
    valor.append(int(input('Digite um numero: ')))

max_valor = max(valor)   
min_valor =min(valor)
print(f'O maior valor digitado foi: {max_valor} na posição {valor.index(max_valor)+1}') 
print(f'O menor valor digitado foi: {min_valor} na posição {valor.index(max_valor)+1}')
