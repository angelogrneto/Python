num = int(input('Digite um termo: '))
razao = int(input('Digite a razao: '))
decimo = num + (10-1) * razao #Formula para calulcar razao até o decimo termo 


for sequencia in range(num,decimo, razao):
    
    print(sequencia)


