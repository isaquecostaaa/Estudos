from src.crud.autores import adicionar_autor, consultar_autores, atualizar_autor, excluir_autor

def menu_autores():
    while True:
        print("\nMENU DE AUTORES")
        print("1 - Consultar autores")
        print("2 - Adicionar autor")
        print("3 - Atualizar autor")
        print("4 - Excluir autor")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                consultar_autores()
            case "2":
                adicionar_autor()
            case "3":
                atualizar_autor()
            case "4":
                excluir_autor()
            case "0":
                break
            case _:
                print("Escolha inválida, tente novamente")

def menu_update_autores():

    print("\nATUALIZAR AUTOR")
    print("1 - Atualizar nome")
    print("2 - Atualizar país de origem")
    print("0 - sair")

    opcao = input("Escolha uma opção: ")
    return opcao