'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

vetor = []

for i in range(0, 10):
    vetor.append(float(input(f'Digite o {i + 1}° número do vetor: ')))

vetor_invertido = list(reversed(vetor))

print(vetor_invertido)