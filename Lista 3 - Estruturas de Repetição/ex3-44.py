'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

# Candidatos e contador de votos
candidatos = {1: 'João', 2: 'Pedro', 3: 'Victor', 4: 'Eduardo', 5: 'Nulo', 6: 'Branco'}
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
cont = 1

while cont == 1:
    # Pede o voto e adiciona ao respecitvo contador de votos
    voto = int(input('Em que candidato você vai votar: '))
    votos[voto] += 1

    cont = int(input('Votar novamente:\n[0] Não\n[1] Sim\n'))

# Imprime lista dos candidatos seus respectivos votos
print('Candidato / N° Votos')
for i in range(1, 7):
    print(f'{candidatos[i]}:    {votos[i]}')

# Imprime os percentuais de nulos e brancos sobre o total de votos
print(f'% Nulos sobre total: {(votos[5]/sum(votos.values())) * 100:.2f}%')
print(f'% Brancos sobre total: {(votos[6]/sum(votos.values())) * 100:.2f}%')