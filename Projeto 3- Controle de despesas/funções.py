def menu():
    opcao = ['Adicionar despesa' , 'Ver despesas' ,  'Sair' ]

    print('=== CONTROLE DE DESPESAS ===\n')
    for item, opcao in enumerate(opcao, start=1 ):

        print(f'{item} - {opcao}')

    while True:
        try:
            escolher = int(input('\nEscolha uma opção? '))

            if 1 <= escolher <= len(opcao):

                return escolher

            else:
                print('opção inválida! Escolha um número entre 1 e 4')

        except ValueError:
            print('opcao invalida, apenas números.')



def dadosDeDespesas(despesas):



    while True:
        dados = {}
        try:
            dados['Nome da despesa'] = str(input('Nome da despesa: '))
            dados['Despesa'] = float(input('Quanto foi a despesa R$: '))
            despesas.append(dados)

        except ValueError:
            print('valores invalidos.\n')
            continue


        continuar = str(input('\nDeseja continuar? [Sim/Não] ')).strip().upper()[0]

        while continuar != 'S' and continuar != 'N':
            continuar = str(input('opcão invalida. Deseja continuar? [Sim/Não] ')).strip().upper()[0]

        if continuar == 'N':
            break

    return despesas




def ver_despesas(despesas):
    total = 0
    for dados in despesas:
        print(f'\nNome: {dados["Nome da despesa"]} - R$ {dados["Despesa"]} ')
        total += dados["Despesa"]

    print(f'\nO total gasto foi de R${total:.2f}')

    return total

