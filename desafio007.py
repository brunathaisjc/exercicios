#Desafio 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule a sua média.

notaUm = int(input('Primeira nota: '))
notaDois = int(input('Segunda nota: '))

media = (notaUm + notaDois) / 2
print('*'*30)
print(f'A primeira nota é: {notaUm}\nA segunda nota é: {notaDois}\nA média é: {media}')

if media <= 6:
    print('*'*30)
    print(f'Deixa de se fazer de burra e vai estudar, poha.')
    print('*'*30)

else:
    print('*'*30)
    print(f'Não fez mais que sua obrigação.')
    print('*'*30)
