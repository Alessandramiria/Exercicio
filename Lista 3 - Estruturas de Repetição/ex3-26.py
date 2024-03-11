'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

# Solicita o número de eleitores e estabele as váriveis para acumular votos dos candidatos
n_eleitores = int(input('Qual o número de eleitores? '))
votos_a = 0
votos_b = 0
votos_c = 0

# Pergunta o voto e soma ao respectivo candidato
for n in range(1, n_eleitores + 1):
    voto = 0
    print('Em que você vota?')
    voto = int(input('[1] Candidato A\n[2] Candidato B\n[3] Candidato C\n'))
    if (voto == 1):
        votos_a += 1
    elif (voto == 2):
        votos_b += 1
    elif (voto == 3):
        votos_c += 1

# Imprime o resultado
print('-=-' * 9)
print('Resultado da eleição:')
print(f'Candidato A: {votos_a} votos\nCandidato B: {votos_b} votos\nCandidato C: {votos_c} votos')
print('-=-' * 9)