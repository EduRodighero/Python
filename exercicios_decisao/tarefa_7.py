""" Faça um programa que leia 2 números e em seguida pergunte ao usuário 
qual operação ele deseja realizar."""

n_1 = float (input('Valor 1: '))
n_2 = float (input('Valor 2: '))

mensagem_opcao = 'O que deseja fazer: 1 - Somar, 2 - Subtrair, 3 - Dividir,  4 - Multiplicar, 0 - Sair'

valor_digitado = f'Os valores Informados Respectivamentes são: {n_1} e {n_2}'

print(mensagem_opcao)
opcao = int (input('Digite o numero correspondente a opção acima: '))

if opcao == 1:
    somar = n_1 + n_2
    print('')
    print(valor_digitado)
    print('Você escolher a Opção Somar!')
    print(f'o Valor da soma é: {somar:.2f}')
elif opcao == 2:
    subtrair = n_1 - n_2
    print('')
    print(valor_digitado)
    print('Você escolher a Opção Subtrair!')
    print(f'o Valor da Subtração é: {subtrair:.2f}')
elif opcao == 3:
    div = n_1 / n_2
    print('')
    print(valor_digitado)
    print('Você escolher a Opção Dividir!')
    print(f'o Valor da Divisão é: {div:.2f}')
elif opcao == 4:
    mult = n_1 * n_2
    print('')
    print(valor_digitado)
    print('Você escolher a Opção Multiplicar!')
    print(f'o Valor da Multiplicação é: {mult:.2f}')
elif opcao == 0:
    print('')
    print(valor_digitado)
    print('Nada a ser Feito, Até Mais!')
else:
    print('')
    print('Você Digitou uma Opção Invalida!')