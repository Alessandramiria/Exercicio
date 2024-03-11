'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

numeros = []
produto = 1

for i in range(0, 5):
    numeros.append(int(input(f'Digite o numero: ')))

for n in numeros:
    produto *= n


print(sum(numeros))
print(produto)
print(numeros)