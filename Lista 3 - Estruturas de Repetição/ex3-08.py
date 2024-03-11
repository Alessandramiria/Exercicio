'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

# Importando função 'mean' da biblioteca 'statistics'
from statistics import mean

# Definindo a lista e adicionando o números
lista = []
for n in range(1, 6):
    lista.append(float(input(f'Digite o {n}° número: ')))

# Soma utilizando a função 'sum' built-in
print(f'Soma: {sum(lista)}')

# calculando a média na marra
print(f'Média: {sum(lista) / 5}')

# Calculando a média usando biblioteca statistics
print(f'Média2: {mean(lista)}')
