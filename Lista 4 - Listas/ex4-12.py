'''
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

# Estabelece listas para armazenar idades e alturas e o contador para alunos que atendam o critério
idades = []
alturas = []
contador_alunos = 0

# Armazena as idades e respectivas alturas
for i in range(0, 5):
    idades.append(int(input(f'Idade do {i + 1}° aluno: ')))
    alturas.append(float(input(f'Altura do {i + 1}° aluno: ')))

# Calcula a média da altura
media_altura = round(sum(alturas)/len(alturas), 2)

# Itera as listas para saber quais alunos são maiores que 13 anos e estão abaixo da altura média
for i in range(0, len(idades)):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador_alunos += 1

print(media_altura)
print(contador_alunos)