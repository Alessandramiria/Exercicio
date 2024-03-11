'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []

for i in range(0, 4):
    notas.append(float(input(f'Digite a {i + 1}° nota: ')))

print(f'Notas: {notas}')
print(f'Média: {sum(notas)/len(notas):.2f}')