#Faça um programa que  leia a largura e a quatidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura

quantidTinta = area / 2


print(f'A sua parede tem:\nAltura: {altura:.2f}m²\nLargura: {largura:.2f}m²\nTinta necessária: {quantidTinta:.2f}l ')