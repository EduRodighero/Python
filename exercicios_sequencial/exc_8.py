"""Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:"""

valor_hora = float (input('Quanto Ganhas por Hora? '))

total_horas = int (input('Quantas Horas Trabalhas no mes ? '))

total_bruto = valor_hora * total_horas

valor_inss = total_bruto * 0.08

valor_ir = total_bruto * 0.11

valor_sindicato = total_bruto * 0.05

total_descontos = valor_inss + valor_sindicato + valor_ir

total_liquido = total_bruto - total_descontos

mensagem_1 = f'O salario Bruto é: {total_bruto:.2f}'
mensagem_2 = f'O Valor pago ao INSS é: {valor_inss:.2f}'
mensagem_3 = f'O valor pago ao Imposto de Renda é: {valor_ir:.2f}'
mensagem_4 = f'O Valor pago ao sindicato é: {valor_sindicato:.2f}'
mensagem_5 = f'O total de Descontos é: {total_descontos:.2f}'
mensagem_6 = f'O Valor liquido é {total_liquido:.2f}'

print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
print(mensagem_4)
print(mensagem_5)
print(mensagem_6)