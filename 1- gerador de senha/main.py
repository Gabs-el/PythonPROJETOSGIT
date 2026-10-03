import random

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*:;?/|><.,=+-_'

senha= ''

while len(senha)  <  tamanho:


    rand = random.choice(caracteres)
    senha += rand

print(f'Sua senha agora é: {senha}')










