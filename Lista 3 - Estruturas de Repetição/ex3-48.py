'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''
# Pede o número desejado
numero = int(input('Digite o número inteiro que deseja inverter: '))

# Cria uma variável para armazenar o resultado
resultado = ''

# Transforma o número em uma lista para que possa ser iterado
reverso = list(str(numero))
reverso.reverse()

# Junta o elemento da lista em um único item e associa a variável resultado
resultado = int(resultado.join(reverso))

# Imprime
print(f'{resultado}')
