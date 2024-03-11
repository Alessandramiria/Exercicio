'''
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

# Lista de meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Lista para armazenar as temperaturas e um dicionário para armazenar mês e respectiva temperatura
temperaturas = []
temperaturas_acima_media = {}

# Loop para solicitar temperaturas
for i in range(0, 12):
    temperaturas.append(float(input(f'Digite a temperatura de {meses[i]}: ')))

# Cálculo da média
temperatura_media = round(sum(temperaturas)/len(temperaturas), 2)

# Loop para verificar quais temperaturas estão acima da média
for i in range(0, 12):
    if temperaturas[i] > temperatura_media:
        temperaturas_acima_media[meses[i]] = temperaturas[i]

print(f'Temperatura média: {temperatura_media}° C')
print(f'Meses acima da média(°C): {temperaturas_acima_media}')