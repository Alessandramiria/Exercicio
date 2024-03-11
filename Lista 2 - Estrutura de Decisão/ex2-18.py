#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import date

data = str(input('Digite a data (dd/mm/aaaa): '))

lista = data.split("/")

try :
    data_valida = date(int(lista[2]), int(lista[1]), int(lista[0]))
except ValueError:
    print('Data inválida.')
    exit()

print(f'A data {data_valida} é válida')