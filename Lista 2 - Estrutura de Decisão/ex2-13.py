dia = int(input('Número de 1 à 7: '))

semana = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}

if dia >= 1 and dia <= 7:
    print(semana[dia])
else:
    print('Número inválido')
