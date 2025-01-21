#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quanto vc tem de dinheiro? '))
dolar = carteira/6.09
print(f'Você tem {carteira} reais. Esse valor corresponde a {dolar:.2f}')


'''
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 6.09
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
'''