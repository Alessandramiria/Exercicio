'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 ou se
é maior que 60; e então, conforme a média calculada, diga se a turma é jovem, adulta ou idosa.
'''

# Solicita o número de pessoas na turma e estabele um dicionário para associar nome a idade
n_pessoas = int(input('Quantas pessoas existem na turma? '))
turma = {}

# Para cada pessoa na turma solicita um nome (chave do dicionário)
# e insere no dicionário a idade (como value). A variável nome é limpa a cada iteração
for i in range(1, n_pessoas + 1):
    nome = ''
    nome = str(input(f'Qual o nome do {i}° aluno? '))
    turma[nome] = int(input(f'Qual a idade do {i}° aluno? '))

# Calcula a média usando acessando apenas os valores do dicionário
media = round((sum(turma.values()))/len(turma.values()), 2)

# Define se a turma é jovem, adulta ou idosa com base na média de idade
print(f'A média de idade da turma é {media} anos.')
if (0 <= media <= 25):
    print('A turma é jovem.')
elif(26 <= media <= 60):
    print('A turma é adulta.')
else:
    print('A turma é idosa.')