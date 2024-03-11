'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

# Solicita o número N de notas que deseja adicionar e define a lista para armezar as notas
n_notas = int(input('Quantas notas deseja adicionar? '))
lista_notas = []

# Roda o loop e armazena nota a nota na lista
for i in range(1, n_notas + 1):
    lista_notas.append(int(input(f'Adicione a {i}° nota: ')))

# imprime o resultado da soma das notas na lista divido pela quantidade de notas.
print(f'A média das notas é {sum(lista_notas) / len(lista_notas)}')