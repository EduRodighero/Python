"""João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com a mensagens adequadas."""

Valor_limite = 50

total_kg = float (input('Digite a quantidade de Kg de peixe pescados: '))

diferenca = total_kg - 50

multa = diferenca * 4

mensagem = f'O valor em Kg de peixe é {total_kg} kg pescados exedendo o total de {diferenca} kg(s) sendo necessario pagar a multa no valor de {multa} Reais!'

print (mensagem)
