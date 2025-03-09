#Crie um programa  que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math

nu = float(input("digite um núero real: "))

nu_int = math.trunc(nu) # math.trunc(x): Corta a parte decimal e mantém apenas a parte inteira.
nu_int_arredondada = math.floor(nu) # math.floor(x): Apenas se for um número negativo ele arredonda para baixo (pega o menor inteiro mais próximo).

print('*'*30)
print(f'O número real digitado é: {nu}\nSua porção inteira é: {nu_int}')
print('*'*30)
print(f'O número real digitado é: {nu}\nSua porção inteira mais próxima é: {nu_int_arredondada}')


