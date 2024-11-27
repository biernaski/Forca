def jogar():
    print("HERE")


def menu():
    while True:
        print("\nSeja bem vindo ao jogo da forca.")
        print("Selecione a opção:\n1 - Jogar\n2 - Sair")
        opcao = input("Digite o numero: ")

        if opcao == '2':
            print("Obrigado por jogar.\n")
            break
        elif opcao != '1':
            print("Opção inváilida. Tente novamente...\n")
        else:
            jogar()