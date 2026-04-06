"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

lata_litro = 18
valor_lata = 80

area = float (input('Informe em metros Quadrados a area a ser pintada: '))

total_litro = area / 3
total_latas = total_litro / 18
total_valor = total_latas * valor_lata

mensagem = f'Total de latas a serem compradas é {total_latas:.2f} lata(s) ficando um custo de {total_valor:.2f} Reais'
print(mensagem)
