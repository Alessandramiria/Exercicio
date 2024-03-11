'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

# Define lista para conter nome do atleta e seus resultados e a lista dos resultados
atleta = []
resultados = []

# Adiciona nome do atleta na primeira lista e adiona a lista de resultados dentro da primeira lista
atleta.append(str(input('Nome do atleta: ')))
atleta.append(resultados)

# Pede todos os saltos
for i in range(0, 5):
    resultados.append(float(input(f'Distância do {i + 1}° salto em metros: ')))

# Cria uma lista paralela para calcular a média sem perder o valor de todos os saltos
resultados_tratados = resultados
resultados_tratados.pop(resultados.index(max(resultados_tratados)))
resultados_tratados.pop(resultados.index(min(resultados_tratados)))

media = round(sum(resultados_tratados) / len(resultados_tratados), 2)

# Imprime tudo
print(f'Atleta: {atleta[0]}')
for i in range(0, 5):
    print(f'{i + 1}° Salto: {resultados[i]} m')

print(f'\nMelhor salto: {max(resultados)} m')
print(f'Pior salto: {min(resultados)} m')

print(f'Média dos demais saltos: {media} m')

print('\nResultado final:')
print(f'{atleta[0]}: {media} m')