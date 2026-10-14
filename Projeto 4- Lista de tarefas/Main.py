from Funcões import *

def main():

    tarefas = []
    while True:
        opcao = menu()

        if opcao == 1:
            adicionar_tarefa(tarefas)

        elif opcao == 2:
            ver_tarefas(tarefas)

        elif opcao == 3:
            remover_tarefas(tarefas)

        elif opcao == 4:
            break

if __name__ == '__main__':
    main()