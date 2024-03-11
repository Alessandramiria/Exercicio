'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

n = int(input('Digite um número inteiro: '))

cent = n // 100
dez = (n % 100) // 10
uni = ((n % 100) % 10) % 10

saida = f'O número {n} possui: '

if cent > 0:
    if cent > 1:
        saida += f'{cent} centenas'
    else:
        saida += f'{cent} centena'
    if dez == 0 and uni == 0:
        saida += '.'

if dez > 0:
    if cent > 0 and uni == 0:
        saida += ' e '
    if cent > 0 and uni > 0:
        saida += ', '
    if dez > 1:
        saida += f'{dez} dezenas'
    else:
        saida += f'{dez} dezena'
    if uni == 0:
        saida += '.'

if uni > 0:
    saida += ' e '
    if uni > 1:
        saida += f'{uni} unidades.'
    else:
        saida += f'{uni} unidade.'

print(saida)
