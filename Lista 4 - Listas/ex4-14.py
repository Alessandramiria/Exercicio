'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

# Lista de perguntas
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?',
             'Devia para a vítima?', 'Já trabalhou com a vítima?']

# Lista de status do interrogado
status = ['Inocente', 'Inocente', 'Suspeita', 'Cúmplice', 'Cúmplice', 'Assassino']

# Contador de respostas positivas
nivel_culpa = 0

# Loop para coletar respotas
for p in perguntas:
    print(p)
    reposta = int(input('[0] - Não\n[1] - Sim\n'))
    if reposta == 1:
        nivel_culpa += 1

# Imprime o status do interrogado conforme seu nível de culpa.
print(f'O interrogado é: {status[nivel_culpa]}')