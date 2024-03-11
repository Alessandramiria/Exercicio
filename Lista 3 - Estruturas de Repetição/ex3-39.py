'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em centímetros. Encontre
o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do
aluno mais baixo, junto com suas alturas.
'''

# Cria o loop
for i in range(0, 10):
    # Pede número do aluno e altura
    numero = int(input('Informe o numero do aluno: '))
    altura = int(input('Informe a altura do aluno: '))

    # vars() é uma função built-in que retorna todas os objetos criados.
    # Verifica se a altura do aluno é maior ou menor do que as alturas estabelecidas
    if ('mais_alto' not in vars()) or (altura > mais_alto):
        mais_alto = altura
        codigo_mais_alto = numero
    if ('mais_baixo' not in vars()) or (altura < mais_baixo):
        mais_baixo = altura
        codigo_mais_baixo = numero

print(f'O aluno mais alto é o de número {codigo_mais_alto} com {mais_alto}')
print(f'O aluno mais baixo é o de número {codigo_mais_baixo} com {mais_baixo}')