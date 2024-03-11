'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores
para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o
desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação
dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem
de programação Python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica
que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo,
mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

O total de votos computados;
Os números e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número
de votos e o percentual de votos dados a ele. Observe que os votos inválidos e o zero
final não devem ser computados como votos. O resultado aparece ordenado pelo número
do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo
do percentual de cada jogador através de uma função. Esta função receberá
dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará
o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são
fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar
os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma
disposição apresentada na tela.
'''

# Lista para contar votos dos jogadores
votos_jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Função para calcular percentual
def percentual(a, b):
    return round((a/b), 2) * 100

# Loop para coletar votos
while True:
    voto = int(input('Número do jogador: '))
    if (voto < 0) or (voto > 23):
        print('Digite um número válido entre 1 e 23 ou 0 para sair.')
    elif (voto == 0):
        break
    else:
        votos_jogadores[voto - 1] += 1

# Soma o total de votos
total_votos = sum(votos_jogadores)

# Abre o arquivo para salvar resultado
arquivo = open('Resultado Votação.txt', 'w')

# Imprime no resultado no arquivo, equivalente ao print do console
arquivo.write(f'Total de votos: {total_votos}\n')

# Imprime resultado
arquivo.write('Jogador - Votos - (%)\n')
for i in range(0, 23):
    # So imprime o número do jogador se ele tiver votos.
    if votos_jogadores[i] != 0:
        arquivo.write(f'{i + 1}' + '         ' if (i + 1) < 10 else f'{i + 1}' + '        ')
        arquivo.write(f'{votos_jogadores[i]}' + '        ')
        arquivo.write(f'{percentual(votos_jogadores[i], total_votos)}%\n')
    else:
        pass


# Fecha o arquivo
arquivo.close()


