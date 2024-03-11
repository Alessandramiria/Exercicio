'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''

n = int(input('Digite um número inteiro: '))

print(f'O número {n} é par.') if n % 2 == 0 else print(f'O numero {n} é ímpar.')