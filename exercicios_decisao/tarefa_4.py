# Faça um programa que leia três números e mostre o maior deles:

n_1 = float(input('Numero 1: '))
n_2 = float(input('Numero 2: '))
n_3 = float(input('Numero 3: '))

mensagem_1 = f'Primeiro numero é o maior: {n_1}'
mensagem_2 = f'Segundo numero é o maior: {n_2}'
mensagem_3 = f'Terceiro numero é o maior: {n_3}'

if n_1 > n_2 and n_1 > n_3:
    print(mensagem_1)
elif n_2 > n_3:
    print(mensagem_2)
else:
    print(mensagem_3)

