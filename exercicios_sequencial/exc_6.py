# Tendo como dados de entrada um arquivo em Gigabytes,
# construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

giga = int (input('Digite a quantidade de Gigabytes: '))

mega = giga * 1024

mensagem = f'A quantidade de Megabytes é: {mega}'

print(mensagem)
