# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
import math

nu1 = float(input('digita o cateto oposto: '))
nu2 = float(input('digita o cateto adjacente: '))


raiz_cateto_oposto = math.sqrt(nu1)
raiz_cateto_adjacente = math.sqrt(nu2)

hipotenusa = math.sqrt(raiz_cateto_adjacente + raiz_cateto_oposto)

print(hipotenusa)
'''
# hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")



