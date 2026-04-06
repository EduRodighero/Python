# Faça um programa que peça dois números e imprima o maior deles.

valor_um = float(input('Valor 1: '))
valor_dois = float(input('Valor 2: '))

if valor_um > valor_dois:
    print('Valor 1 Maior', valor_um)
elif valor_um < valor_dois:
    print('valor 2 maior', valor_dois)
else:
    print('Valores são iguais!')