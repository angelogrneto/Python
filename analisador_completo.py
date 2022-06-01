media = 0
homem_velho_idade = 0
nome_homem_velho = ''
mulher_20 = 0
nome_mulher = ''
soma_mulher = 0

for p in range(1,4):
    print('----- {} Pessoa -----'.format(p))
    nome = str(input('Nome: ')).split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media = (idade * p) / 3

    if p == 1 and sexo in 'Mm':
        homem_velho_idade = idade
        nome_homem_velho = nome
    if sexo in 'Mn' and idade > homem_velho_idade:
        homem_velho_idade = idade
        nome_homem_velho = nome
    if sexo in "Ff" and idade <=20:
        
        nome_mulher = nome
        soma_mulher = soma_mulher + 1
        
       

print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_velho_idade, nome_homem_velho))
print('Tem {} mulheres abaixo dos 20 anos'.format(soma_mulher))