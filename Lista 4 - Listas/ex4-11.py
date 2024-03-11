'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

# Define listas para armazenar os elementos
vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_resultado = []

# Adiciona os elementos no primeiro vetor
for i in range(0, 10):
    vetor_1.append(input(f'1° Vetor - {i + 1}° elemento: '))

# Adiciona os elementos no segundo vetor
for i in range(0, 10):
    vetor_2.append(input(f'2° Vetor - {i + 1}° elemento: '))

# Adiciona os elementos no terceiro vetor
for i in range(0, 10):
    vetor_3.append(input(f'2° Vetor - {i + 1}° elemento: '))

# Intercala elementos dos vetores em um terceiro vetor
for i in range(0, 10):
    vetor_resultado.append(vetor_1[i])
    vetor_resultado.append(vetor_2[i])
    vetor_resultado.append(vetor_3[i])

print(vetor_resultado)