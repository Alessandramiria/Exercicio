"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1 - "Telefonou para a vítima?"
2 - "Esteve no local do crime?"
3 - "Mora perto da vítima?"
4 - "Devia para a vítima?"
5 - "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?',
             'Devia para a vítima?', 'Já trabalhou com a vítima?']
classificacao = 0

for i in range(0, 5):
    print(perguntas[i])
    classificacao += int(input('[0] Sim\n[1] Não\n'))

if classificacao <= 1:
    print('Inocente')
elif classificacao == 2:
    print('Suspeito')
elif classificacao == 3 or classificacao == 4:
    print('Cúmplice')
else:
    print('Assassino')
