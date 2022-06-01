from tkinter import N


nome = input('Digite seu nome: ')

#print('É um prazer te conhecer', nome)

print('é um prazer te conhecer, {}!'.format(nome))

print('o tipo primitivo desse valor é: ', type(nome))
print('só tem espaços? ', nome.isspace())
print('é um numero?', nome.isnumeric())
print('é alfabetico?, ', nome.isalpha())
print('é alfanumerico? ', nome.isalnum())
print('esta em maiscula? ', nome.isupper())
print('esta em minuscula? ', nome.islower())
print('esta em capitalizada? ', nome.istitle())


