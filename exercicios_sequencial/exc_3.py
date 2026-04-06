# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

valor_lado = int (input('Qual a medida do lado do quadrado?: '))
area = valor_lado ** 2
area_dois = area * 2

print( f'A area do quadrado é {area}')
print( f'A area Vezes 2 é: {area_dois}')