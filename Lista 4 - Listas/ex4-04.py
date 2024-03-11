'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
'''

# Define lista de consoantes, contador de consoantes e lista de consoantes contadas
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'x', 'y', 'w', 'z', 'ç')
contador_consoantes = 0
consoantes_contadas = []
cont = True

# Enquanto não for digitado uma string com 10 caracteres o programa continua pedindo um novo string
while cont:
    string = str(input('Digite uma string de 10 caracteres: ')).lower()

    if len(string) != 10:
        print('O string deve ter 10 caracteres.')
    else:
        cont = False

# Loop para verificar se cada caracter está contido na lista de consoantes.
for caracter in string:
    if caracter in consoantes:
        contador_consoantes += 1
        consoantes_contadas.append(caracter)

# Imprime resultado
print(f'Foram contadas um total de {contador_consoantes} consoantes.')
print(f'São elas: {consoantes_contadas}')
