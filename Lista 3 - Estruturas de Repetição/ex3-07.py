'''
Faça um programa que leia 5 números e informe o maior número.
'''

# Lista para armazenar números
lista = []

# Solicita números
for n in range(1, 6):
    lista.append(float(input(f'Digite o {n}° número: ')))

# Imprime maior número da lista
print(max(lista))