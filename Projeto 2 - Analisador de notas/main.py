def media_notas():


    nome = input('Nome do aluno: ').strip().lower()

    while True:

        try:

            nota1 = float(input('Primeira nota: '))
            nota2 = float(input('Segunda nota: '))

            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                print('Valor invalido apenas de 0 a 10')

            else:
                break

        except ValueError:
            print('Valor incorreto, apenas numeros')


    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f'O aluno {nome} foi aprovado com a média {media:.2f}')

    elif media >= 5:
        print(f'O aluno {nome}, está de recuperação com a média {media:.2f}')


    else:
        print(f'O aluno {nome}, está reprovado com a média {media:.2f}')

    return media


aluno1 = media_notas()
