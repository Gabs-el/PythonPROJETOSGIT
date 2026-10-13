from funções import menu,dadosDeDespesas,ver_despesas
despesas = []



while True:
    opcao = menu()

    if opcao == 1:
        dadosDeDespesas(despesas)

    elif opcao == 2:
        ver_despesas(despesas)

    elif opcao == 3:
        break