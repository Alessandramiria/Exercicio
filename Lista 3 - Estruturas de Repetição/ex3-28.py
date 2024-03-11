'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção
de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade
de CDs e o valor para em cada um.
'''

# Estabelece número de CDs da coleção e o dicionário que vai armazenar cd e valor
n_cds = int(input('Quantos CDs existem na coleção? '))
colecao = {}

# Pergunta o nome do cd e o adiona com o seu respecitvo valor no dicionário
for i in range(1, n_cds + 1):
    nome_cd = str(input(f'Nome do {i}° CD: '))
    colecao[nome_cd] = float(input(f'Quanto {nome_cd} custou? '))

# Calcula média e imprime resultados
media = round(sum(colecao.values()) / len(colecao.values()), 2)
print(f'A coleção inteira custou R${sum(colecao.values())} e o valor médio por CD foi de R${media}')