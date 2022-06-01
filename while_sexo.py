sexo = input('Digite o sexo [M/F]: ').strip()

while sexo not in "MnFf":
    sexo = input('Sexo ivalido digite o sexo novamente [M/F]: ').strip()

print('Sexo registrado')
