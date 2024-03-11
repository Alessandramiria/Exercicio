'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia um conjunto indeterminado de temperaturas, e informe ao final a menor
e a maior temperaturas informadas, bem como a média das temperaturas.
'''

# Define lista para armanzenar temperaturas
lista_temperaturas = []

# Loop infinito para adicionar as temperaturas e mostrar as informações solicitadas a cada novo registro
while True:

    lista_temperaturas.append(float(input('Digite a temperatura(°C): ')))
    print(f'A maior temperatura registrada foi: {max(lista_temperaturas)}°C')
    print(f'A menor temperatura registrada foi: {min(lista_temperaturas)}°C')
    print(f'A média das temperaturas registradas é: {round(sum(lista_temperaturas)/len(lista_temperaturas),2)}°C')
