from src.crud.usuarios import cadastrar_usuario, consultar_usuarios, atualizar_usuario, excluir_usuario

def menu_usuarios():
    while True:
        print("\nMENU DE USUÁRIOS")
        print("1 - Consultar usuários")
        print("2 - Adicionar usuário")
        print("3 - Atualizar usuário")
        print("4 - Excluir usuário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                consultar_usuarios()
            case "2":
                cadastrar_usuario()
            case "3":
                atualizar_usuario()
            case "4":
                excluir_usuario()
            case "0":
                break
            case _:
                print("Escolha inválida, tente novamente")

def menu_update_usuarios():
        print("\nATUALIZAR AUTOR")
        print("1 - Atualizar nome")
        print("2 - Atualizar sobrenome")
        print("3 - Atualizar data de nascimento")
        print("0 - sair")

        opcao = input("Escolha uma opção: ")

        return opcao