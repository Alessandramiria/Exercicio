'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto
por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se
outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite
o gabarito da prova antes dos alunos usarem o programa.
'''

# Já fiz a versão melhorada da questão
# Definindo listas com gabarito, uma lista para guardar as respostas dos alunos e outra as notas
gabarito = []
respostas_alunos = []
notas_alunos = []
cont = True

# Adicionando o gabarito
print(f'Por favor digite o gabarito da prova')
for i in range(0, 10):
    gabarito.append(str(input(f'Respota da {i + 1}° questão: ')).lower())

while cont:
    # Defini uma lista temporária para guardar as respostas de cada aluno
    respostas = []

    # Adicionando as respostas de cada aluno na lista
    print('Repostas do aluno:')
    for i in range(0, 10):
        respostas.append(str(input(f'{i + 1}° pergunta: ').lower()))

    # Adicionando a lista com as respostas do aluno, na lista maior que defininda no início.
    respostas_alunos.append(respostas)

    # Se desejar adicionar as respostas de outro aluno, o sistema volta para começo do loop
    # e redefine a lista temporária como vazia para começar de novo
    cont = True if int(input('Deseja adiocionar a nota de um aluno?\n[0] - Sim\n[1] - Não\n')) == 0 else False

# Corrige as notas dos alunos, comparando gabarito com cada resposta
for i in range(0, len(respostas_alunos)):
    nota = 0
    for r in range(0, len(respostas_alunos[i])):
        if respostas_alunos[i][r] == gabarito[r]:
            nota += 1

    notas_alunos.append(nota)

# Imprime as saídas pedidas
print(f'Número de alunos que fizeram o teste {len(notas_alunos)}')
print(f'Maior nota{max(notas_alunos)}')
print(f'Menor nota {min(notas_alunos)}')
print(f'Média da turma {sum(notas_alunos)/len(notas_alunos):.2f}')
print(gabarito)

