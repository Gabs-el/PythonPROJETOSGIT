def menu():
    menu = ['Adicionar', 'Ver tarefas', 'Remover tarefas', 'sair']

    print('=== LISTA DE TAREFAS ===\n')
    for item,menu in enumerate(menu, start=1):
        print(f'{item} - {menu}')

    while True:

        try:
            escolher = int(input('\nEscolha uma opcão de 1 a 4: '))

            if 1 <= escolher <= len(menu):
                return escolher

            else:
                print('ecolha invalida apenas de 1 a 4')


        except ValueError:
            print('opção invalida apenas numeros')

def adicionar_tarefa(tarefas):
    print('=== ADICIONAR TAREFA ===\n')



    while True:
        dicionario_tarefa = {}

        estatus = ('ATIVO', 'PENDENTE','TERMINADO')

        dicionario_tarefa['Nome da tarefa'] = str(input('Nome da tarefa: '))

        dicionario_tarefa['Status'] = str(input('Status da tarefa [ATIVO/PENDENTE/TERMINADO]:')).strip().upper()
        if dicionario_tarefa['Status'] in estatus:
            tarefas.append(dicionario_tarefa)

        else:
            print('status invalidos apenas [ATIVO/PENDENTE/TERMINADO]')




        continuar = str(input('\nDeseja continuar? [Sim/Não] ')).strip().upper()

        while continuar != 'S' and continuar != 'N':
            continuar = str(input('opcão invalida. Deseja continuar? [Sim/Não] ')).strip().upper()

        if continuar == 'N':
            break

    return tarefas


def ver_tarefas(tarefas):
    print('\n=== VER TAREFAS ===\n')

    if not tarefas:
        print('Nenhuma tarefa encontrada!')
        return

    for item,tarefas in enumerate(tarefas, start=1):
        print(f'{item} - {tarefas["Nome da tarefa"]}: {tarefas["Status"]}')

    return

def remover_tarefas(tarefas):
    print('\n=== REMOVER TAREFAS ===\n')

    if not tarefas:
        print('Nenhuma tarefa encontrada!')
        return

    procurar = str(input('qual o nome da tarefa: '))

    for item in tarefas:

        if item["Nome da tarefa"].lower() == procurar.lower():

            while True:
                deseja = str(input('Deseja remover a tarefa? [S/N] ')).strip().upper()

                if deseja in ('S', 'N'):
                    break

                print('Opção inválida! Digite S ou N.')

            if deseja == 'S':
                tarefas.remove(item)
                print('Tarefa removida com sucesso!')

            else:
                print('Remoção cancelada!')

            return

    print('Tarefa não encontrada!')


