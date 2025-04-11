from src.crud.livros import adicionar_livro, consultar_livros, atualizar_livro, excluir_livro

def menu_livros():
    while True:
        print("\nMENU DE LIVROS")
        print("1 - Consultar livros")
        print("2 - Adicionar livro")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                consultar_livros()
            case "2":
                adicionar_livro()
            case "3":
                atualizar_livro()
            case "4":
                excluir_livro()
            case "0":
                break
            case _:
                print("Escolha inválida, tente novamente")

def menu_update_livros():
    
    print("\nATUALIZAR LIVRO:")
    print("1. Título")
    print("2. ISBN")
    print("3. Gênero")
    print("4. Data de Publicação")
    print("5. Quantidade de Páginas")
    print("6. Disponibilidade")
    print("0. Sair")
    
    opcao = input("\nEscolha o campo que deseja atualizar: ")

    return opcao
