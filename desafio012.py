# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto: R$ '))
desconto = float(input('Porcentagem do desconto: '))
valorDesconto = (preco * desconto) / 100

novoPreco = preco - valorDesconto

print(f'Preço original: R$ {preco:.2f}\nDesconto: R$ {desconto:.2f}\nVocê irá pagar apenas R$ {novoPreco:.2f}')


