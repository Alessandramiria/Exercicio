'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

# Solicita quantos números serão adicionados ao conjunto
qntd = int(input('Quantos números deseja adicionar? '))
# Define o conjunto, incialmente vazio
lista = []

# Adiona os números inteiros ao conjunto um a um.
for i in range(0, qntd):
    lista.append(int(input(f'Digite o {i + 1}° número: ')))

# Imprime a soma, o maior e o menor valor do conjunto
print(f'A soma dos números do conjunto é {sum(lista)}')
print(f'O maior valor do conjuto é: {max(lista)}')
print(f'O menor número do conjunto é: {min(lista)}')