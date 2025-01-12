'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possíveis sobre ele'''

nome = 'Brunelda'
print('O tipo desta variável é: ',type(nome))
print('Tem espaço? ',nome.isspace())
print('É numérico?', nome.isnumeric())
print('É decimal?',nome.isdecimal())
print('É alfabético?',nome.isalpha())
print('É alfanumérico',nome.isalnum())
print('Tem todos os caracteres maiúsculos?',nome.isupper())
print('Tem todos os caracteres minúsculos?',nome.islower())
print('Está capitalizada?',nome.istitle())



