'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''

alturas = []
idades = []

for i in range(0, 5):
    idades.append(int(input(f'Digite a idade da {i + 1}° pessoa: ')))
    alturas.append(float(input(f'Digite a altura da {i + 1}° pessoa: ')))

alturas_inverso = list(reversed(alturas))
idades_inverso = list(reversed(idades))

print(alturas_inverso)
print(idades_inverso)