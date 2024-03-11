'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

# Pede usuário e senha
nome_usuario = str(input('Digite um nome de usuário: '))
senha = str(input('Digite uma senha: '))

# Verifica se usuário e senha são iguais. Enquanto estiverem iguais informa e solicita novamente
while (nome_usuario == senha):
    print('Nome de usuário e senha não podem ser iguais. Digite novamente:')
    nome_usuario = str(input('Digite um nome de usuário: '))
    senha = str(input('Digite uma senha: '))

print('Nome de usuário e senha são validos')