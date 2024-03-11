'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores
com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma
semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um
programa (usando um array de contadores) que determine quantos vendedores receberam
salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

# Define lista com os patamares de pagamento, contadores e uma lista para armazenar o quanto cada vendedor recebeu
intervalos = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000, 2000]]
contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
pagamentos = []
n = 0
cont = True

while cont:
    pagamentos.append(float(input('Digite o pagamento do vendador: ')))
    # Para cada pagamento, faz um loop para verificar em qual intervalo ele se encontra e
    # adiciona +1 ao respectivo contador
    for x in range(0, len(intervalos)):
        if intervalos[x][0] <= pagamentos[n] <= intervalos[x][1]:
            contadores[x] += 1

    n += 1
    cont = True if input('Deseja continuar(S/N)? ').upper() == 'S' else False

# Imprime os contadores
for i in range(0, len(contadores)):
    print(f'{contadores[i]} vendedores ganham entre {intervalos[i][0]} e {intervalos[i][1]} reais')

# Descobre em que patamar da lista um salário está
salario = float(input('Digite um salário: '))
for i in range(0, len(intervalos)):
    if intervalos[i][0] <= salario <= intervalos[i][1]:
        print(f'Você está no {i + 1}° da lista')

    elif salario < intervalos[0][0]:
        print('Você não vendeu nada.')
        break
