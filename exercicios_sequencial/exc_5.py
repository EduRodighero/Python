# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

valor_um = int (input('Primeiro valor Interio: '))
valor_dois = int (input('Segundo valor Interio: '))
valor_real = float (input('Primeiro valor Real: '))

parte_um = valor_um * 2 + valor_dois / 2

parte_dois = valor_um * 3 + valor_real

parte_tres = valor_real ** 3

mensagem_1 = f'O produto do dobro do primeiro com metade do segundo é: {parte_um}'
mensagem_2 = f'A soma do triplo do primeiro com o terceiro: {parte_dois}'
mensagem_3 = f'O terceiro elevado ao cubo é: {parte_tres}'

print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
