'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

if n1 < 0 or n1 > 10 or n1 < 0 or n2 > 10 or  n1 < 0 or n2 > 10:
    print('Valor inválido passado como nota.')
    exit()

media = (n1 + n2 + n3) / 3

if media < 7:
    print('Reprovado')
elif 7 <= media < 10:
    print('Aprovado')
else:
    print('Aprovado com Distinção.')