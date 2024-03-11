'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme
a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída
do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

# Define lista para conter nome do atleta e seus resultados e a lista dos resultados
atleta = []
resultados = []

# Adiciona nome do atleta na primeira lista e adiona a lista de resultados dentro da primeira lista
atleta.append(str(input('Nome do atleta: ')))
atleta.append(resultados)

# Pede todos as notas
for i in range(0, 7):
    resultados.append(float(input(f'Nota do {i + 1}° jurado: ')))

# Cria uma lista paralela para calcular a média sem perder o valor de todos os saltos
resultados_tratados = resultados
resultados_tratados.pop(resultados.index(max(resultados_tratados)))
resultados_tratados.pop(resultados.index(min(resultados_tratados)))

media = round(sum(resultados_tratados) / len(resultados_tratados), 2)

# Imprime tudo
print(f'Atleta: {atleta[0]}')
for i in range(0, 7):
    print(f'{i + 1}° Nota: {resultados[i]}')

print(f'\nMelhor Nota: {max(resultados)}')
print(f'Pior Nota: {min(resultados)}')

print(f'Média das demais notas: {media}')

print('\nResultado final:')
print(f'{atleta[0]}: {media}')
