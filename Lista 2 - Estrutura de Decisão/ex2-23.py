"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

n = float(input('Digite um número: '))

print(f'O número {n} é inteiro') if n.is_integer() else print(f'O número {n} é decimal')
