soma = 0
cont = 0
for numeros in range(0,6):
    numm = int(input('Digite o primeiro numero: '.format(numeros)))
    if numm % 2 == 0:
        soma = soma + numm
        cont = cont + 1 
print('Voce digitou o numero {} e a soma dos numeros PARES é {}'.format(cont,soma))
   
   