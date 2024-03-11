'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

# Define a lista para armazenar a lista de notas e as médias
notas = []
medias = []
contador_aprovados = 0

# Loop para armazenar notas, calcular médias e armazenar as médias
for i in range(0, 10):
    notas_aluno = []
    for n in range(0, 4):
        notas_aluno.append(float(input(f'Digite a {n + 1}° do {i + 1}° aluno: ')))

    medias.append((sum(notas_aluno)/len(notas_aluno)))
    notas.append(notas_aluno)

# Loop para contar quem foi aprovado
for media in medias:
    if media > 7:
        contador_aprovados += 1

print(f'{contador_aprovados} alunos ficaram acima da média.')
