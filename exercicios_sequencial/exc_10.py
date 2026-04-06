"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tam_arq = float(input('Digite o tamanho do arquivo em mb: '))

vel_net = float(input('Digite a velocidade da internet: '))

velo_segundos = tam_arq / vel_net

minuto = velo_segundos / 60

mensagem = f'O tempo em minutos para o download é de: {minuto:.2f} minuto(s) equivalente a {velo_segundos:.2f} segundo(s)'
print(mensagem)
