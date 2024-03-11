'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

# Define lista para armazenar notas e contador de notas acima da média e abaixo de 7
notas = []
acima_da_media = 0
abaixo_de_7 = 0

# Loop para armazenar notas
while True:
    nota = float(input('Digite uma nota: '))
    if (nota == -1):
        break
    else:
        notas.append(nota)

# Imprime quantidade de notas lidas e as notas
print(f'Quantidade de notas lidas: {len(notas)}')
print(notas)

# Cria uma lista com as notas em ordem inversa e imprime uma a uma
notas_invertidas = list(reversed(notas))
for n in notas_invertidas:
    print(n)

# Imprime a soma das notas e média
print(sum(notas))
media_notas = round(sum(notas)/len(notas), 2)
print(media_notas)

# Verifica se as notas estão acima da média cálculada ou abaixo de 7 e incrementa os contadores
for n in notas:
    if n > media_notas:
        acima_da_media += 1
    elif n < 7:
        abaixo_de_7 += 1

# Imprime resultados
print(f'Quantidade de notas acima da média: {acima_da_media}')
print(f'Quantidade de notas abaixo da 7: {abaixo_de_7}')

