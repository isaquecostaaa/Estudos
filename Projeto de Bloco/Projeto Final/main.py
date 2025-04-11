from menus.menu_principal import exibir_menu_principal
from menus.menu_livros import menu_livros
from menus.menu_autores import menu_autores
from menus.menu_emprestimos import menu_emprestimos
from menus.menu_usuarios import menu_usuarios

def menu_principal():
    while True:
        opcao = exibir_menu_principal()
        match opcao:
            case "1":
                menu_livros()
            case "2":
                menu_autores()
            case "3":
                menu_emprestimos()
            case "4":
                menu_usuarios()
            case "0":
                print("Encerrando sistema...")
                break
            case _:
                print("Escolha inválida, tente novamente")

menu_principal()


