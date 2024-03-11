'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''

# Solicita quantidade de turmas e estabelece variável com total de alunos
qntd_turmas = int(input('Quantas turmas deseja utilizar no cálculo da média? '))
qntd_alunos = 0


for i in range(1, qntd_turmas + 1):
    # variável auxiliar. cada iteração ela recebe um novo valor e soma na quantidade total de alunos
    turma_n = int(input(f'Quantos aluno existem na {i}° turma? '))
    while (0 > turma_n) or (turma_n > 40):
        print('A turma não pode conter mais de 40 alunos.')
        turma_n = int(input(f'Quantos aluno existem na {i}° turma? '))
    qntd_alunos += turma_n

media_alunos = int(qntd_alunos / qntd_turmas)

print(f'As turmas tem uma média de {media_alunos} alunos.')
