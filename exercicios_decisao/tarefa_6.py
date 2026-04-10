"""Uma organização resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa
que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""


salario_atual = float(input('Informe seu salario Atual: '))

reajuste_1 = 0.05
reajuste_2 = 0.10
reajuste_3 = 0.15
reajuste_4 = 0.20

mensagem_1 = f'Seu salario antes do reajuste era: {salario_atual:.2f} Reais '
mensagem_1_1 = f'Percentual de reajuste é {reajuste_4 * 100:.0f}%'
mensagem_1_2 = f'Percentual de reajuste é {reajuste_3 * 100:.0f}%'
mensagem_1_3 = f'Percentual de reajuste é {reajuste_2 * 100:.0f}%'
mensagem_1_4 = f'Percentual de reajuste é {reajuste_1 * 100:.0f}%'

if salario_atual < 281:
    aumento = salario_atual * reajuste_4
    salario_novo = salario_atual + aumento
    print(mensagem_1)
    print(mensagem_1_1)
    print(f'O valor do aumento foi de: {aumento:.2f} Reais')
    print(f'O valor do novo salario é: {salario_novo:.2f} Reais')
elif salario_atual > 280 and salario_atual < 701:
    aumento = salario_atual * reajuste_3
    salario_novo = salario_atual + aumento
    print(mensagem_1)
    print(mensagem_1_2)
    print(f'O valor do aumento foi de: {aumento:.2f} Reais')
    print(f'O valor do novo salario é: {salario_novo:.2f} Reais')
elif salario_atual > 700 and salario_atual < 1501:
    aumento = salario_atual * reajuste_2
    salario_novo = salario_atual + aumento
    print(mensagem_1)
    print(mensagem_1_3)
    print(f'O valor do aumento foi de: {aumento:.2f} Reais')
    print(f'O valor do novo salario é: {salario_novo:.2f} Reais')
else:
    aumento = salario_atual * reajuste_1
    salario_novo = salario_atual + aumento
    print(mensagem_1)
    print(mensagem_1_4)
    print(f'O valor do aumento foi de: {aumento:.2f} Reais')
    print(f'O valor do novo salario é: {salario_novo:.2f} Reais')
