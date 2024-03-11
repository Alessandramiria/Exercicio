'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

# Estabelece as listas, e a variável incremental para média
codigos = []
numero_veiculos = []
numero_acidentes = []
media_menor_2000 = 0
contador = 0

# Adiciona os números nas respectivas listas
for i in range(0, 2):
    codigos.append(int(input('Código da cidade: ')))
    numero_veiculos.append(int(input('Número de veículos: ')))
    numero_acidentes.append(int(input('Número de acidentes de trânsito com vítimas: ')))

# Incrementa a variável da media
for i in range(0, len(numero_veiculos)):
    if numero_veiculos[i] < 2000:
        media_menor_2000 += numero_acidentes[i]
        contador += 1
    media_menor_2000 = media_menor_2000 / contador

# Imprime resultados
print(f'O maior número de acidentes é {codigos[numero_acidentes.index(max(numero_acidentes))]}'
      f' da cidade {max(numero_acidentes)} ')
print(f'O maior número de acidentes é {codigos[numero_acidentes.index(min(numero_acidentes))]}'
      f' da cidade {min(numero_acidentes)} ')
print(f'A média de veículos nas 5 cidades é {sum(numero_veiculos)/len(numero_veiculos)}')
print(f'Média de acidentes para cidades com menos de 2.000 veículos: {media_menor_2000}')

