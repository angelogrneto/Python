import random


while True:
    
    para = input('Deseja continuar [S/N]: ').upper().strip()[0]
    

    computador = random.randint(0,10)
    
    print(''' Par ou Impar [P/I]''')
    numero = int(input('Digite um numero: '))
    escolha = input('[P/I]').upper().strip()[0]
    
    soma = numero + computador
    par_impar = soma % 2
    print(computador)

    if escolha == 'P' and par_impar == 0:
        print(f'A soma é {soma} voce venceu, deu PAR')
    
    elif escolha == 'I' and par_impar == 1:
        print(f'A soma é {soma} voce venceu, deu Impar')

    elif computador != par_impar:
        print(f'A soma é {soma} O computador venceu')

