'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = []
resultado = 0

for i in range(0, 10):
    numeros.append(int(input(f'{i + 1}° número: ')))

for n in numeros:
    resultado += (n*n)

print(resultado)