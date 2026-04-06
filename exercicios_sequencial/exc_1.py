# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

total_horas = int (input('Quantas Horas Trabalhadas?: '))
valor_horas = float (input('Quanto vale a sua hora?: '))
dias_trabalhados = int (input ('Quantos Dias Você Trabalhou?: '))

salario = total_horas * valor_horas * dias_trabalhados

print(f'Seu salario esse mês é: {salario}2f')
