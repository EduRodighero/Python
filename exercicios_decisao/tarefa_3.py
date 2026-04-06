"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota_um = float(input('Nota um: '))
nota_dois = float(input('Nota dois: '))

media = (nota_um + nota_dois) / 2

mensagem_apro = 'Aluno Aprovado'
mensagem_apro_10 = 'Aluno SuperAprovado'
mensagem_repro = 'Aluno Reprovado'

if media == 10:
    print(f'{mensagem_apro_10} com nota {media}')
elif media >= 7 and media < 10:
    print(f'{mensagem_apro} com nota {media}')
else:
    print(f'{mensagem_repro} com nota {media}')
