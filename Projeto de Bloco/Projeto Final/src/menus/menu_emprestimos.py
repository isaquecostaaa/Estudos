from src.crud.emprestimos import realizar_emprestimo, consultar_emprestimos, atualizar_emprestimo, excluir_emprestimo


def menu_emprestimos():
    while True:
        print("\nMENU DE EMPRÉSTIMO")
        print("1 - Consultar empréstimos")
        print("2 - Adicionar empréstimo")
        print("3 - Atualizar empréstimo (devolução)")
        print("4 - Excluir empréstimo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                consultar_emprestimos()
            case "2":
                realizar_emprestimo()
            case "3":
                atualizar_emprestimo()
            case "4":
                excluir_emprestimo()
            case "0":
                break
            case _:
                print("Escolha inválida, tente novamente")

def menu_update_emprestimos():

    print("\nATUALIZAR EMPRÉSTIMO")
    print("1 - Atualizar data do empréstimo")
    print("2 - Registrar devolução")
    print("0 - Voltar")

    opcao = input("Escolha uma opção: ")
    return opcao
