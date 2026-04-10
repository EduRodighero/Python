# Faça um programa que leia três números e mostre-os em ordem decrescente:

n_1 = float(input('Numero 1: '))
n_2 = float(input('Numero 2: '))
n_3 = float(input('Numero 3: '))

mensagem_1 = f'A ordem decrescente é: {n_1} {n_2} {n_3}'
mensagem_2 = f'A ordem decrescente é: {n_2} {n_3} {n_1}'
mensagem_3 = f'A ordem decrescente é: {n_3} {n_1} {n_2}'


if n_1 > n_2 and n_1 > n_3 and n_2 > n_3:
    print(mensagem_1)
elif n_2 > n_1 and n_2 > n_3 and n_3 > n_1:
    print(mensagem_2)
else:
    print(mensagem_3)