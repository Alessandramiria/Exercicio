'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
'''

saque = int(input('Digite o valor que deseja sacar: R$'))
saque2 = saque

nota_cem = saque2 // 100
saque2 = saque2 - (nota_cem * 100)

nota_cinq = saque2 // 50
saque2 = saque2 - (nota_cinq * 50)

nota_dez = saque2 // 10
saque2 = saque2 - (nota_dez * 10)

nota_cinc = saque2 // 5
saque2 = saque2 - (nota_cinc * 5)

nota_um = saque2

print(nota_cem, nota_cinq, nota_dez, nota_cinc, nota_um)