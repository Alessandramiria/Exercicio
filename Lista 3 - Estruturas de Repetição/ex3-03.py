'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
# Lista com as opções de sexo e estado civil
lista_sexo = ['f', 'm']
lista_estado_civil = ['s', 'c', 'v', 'd']

# Pede as informações e verifica se estão conforme as condições pre-estabelecidas. Enquanto não estiver,
# informa e solicita novamente
nome = str(input('Nome: '))
while (len(nome) <= 3):
    print('O nome precisa ter mais do que 3 caracteres. Tente novamente.')
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while (idade < 0 or idade > 150):
    print('A idade precisa estar entre 0 e 150 anos. Tente novamente.')
    idade = int(input('Idade: '))

salario = float(input('Salário: '))
while (salario <= 0):
    print('O salário precisa ser maior do que "0". Tente novamente.')
    salario = float(input('Salário: '))

sexo = str(input('Sexo (f/m): ').lower())
while (sexo not in lista_sexo):
    print('O sexo deve ser preenchido como "f" ou "m". Tente novamente.')
    sexo = str(input('Sexo (f/m): '))

# Usei uma lista para o caso do estado civil para diminuir a quantidade de verificações necessárias.
# Bastou verificar se a opção fornecida está dentro da lista.
estado_civil = str(input('Estado civil (s/c/v/d): ').lower())
while (estado_civil not in lista_estado_civil):
    print('O estado civil deve ser preenchido como "s", "c", "v", "d". Tente novamente.')
    estado_civil = str(input('Estado civil (s/c/v/d): '))
