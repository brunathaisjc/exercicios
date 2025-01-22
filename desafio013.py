#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Quanto você ganha? R$ '))
aumento = (salario*15)/100

novoSalario = salario + aumento

print(f'Seu salário atual: R$ {salario}\nCom aumento de 15%: R$ {novoSalario}')