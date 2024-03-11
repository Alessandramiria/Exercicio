'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

# Pede o número para cálculo do fatorial e estabelece a variável que será incrementada
numero = int(input('Fatorial de: '))
fatorial = 1

# Loop para gerar a impressão conforme solicitado no enunciado
print(f'{numero}! = {numero}', end=' ')
for i in range(1, numero):
    print(f'. {numero - i}', end=' ')

# Loop para calcular o fatorial
for i in range(1, numero + 1):
    fatorial *= i

print(f'= {fatorial}')
