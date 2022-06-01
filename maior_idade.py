from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for laco in range(0,3):
    ano = int(input('digite seu ano de nascimento: '.format(laco)))
    maior = data - ano
    if maior >=18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor - 1


print('Numero de pessoas com mais de 18 anos é: {}'.format(totmaior))
print('Numero de pessoas com menos de 18 anos é: {}'.format(totmenor))
    

    
    


