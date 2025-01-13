#Dasafio 5
#Uma breve aulinha sobre operadores aritméticos
'''
5 + 2 == 7 adição
5 - 2 == 3 diminuição
5 * 2 == 10 multiplicação
5 / 2 == 2.5 divisão real
5 ** 2 == 25 (5*5)potenciação
5 // 2 == 2 divisão inteira 
5 % 2 == 1 divisão que mostra apenas o resto

Ordem de precedência
1° () parêntesis
2° ** potenciação
3°  *, /, //, %
4°  + , -
'''
#Faça um programa que leia um number inteiro e mostre na tela o seu sucessor e seu antecessor

numeroUm = int(input('passa um numero ai: '))

sucessor = numeroUm + 1
print(f'O número que você escolheu foi {numeroUm}.\nO sucessor deste número é: {sucessor}')

antecessor = numeroUm - 1
print(f'E o antecessor dele é: {antecessor}')
