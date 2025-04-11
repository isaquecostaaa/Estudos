from src.utils.validar_data import validar_data
from src.crud.usuarios_db import *
from src.crud.emprestimos_db import verificar_emprestimos_ativos

def consultar_usuarios():
    try:
        usuarios = consultar_usuarios_db()

        if usuarios:
            print("-- USUÁRIOS --")
            print("-" * 40)

            for usuario in usuarios:
                id_usuario, nome, sobrenome, data_nascimento = usuario
                print(f"ID: {id_usuario}")
                print(f"Nome: {nome} {sobrenome}")
                print(f"Data de nascimento: {data_nascimento}")
                print("-" * 40)
        else:
            print("Não há usuários cadastrados no banco de dados.")
    except Exception as e:
        print(f"Erro ao consultar usuários: {e}")

def excluir_usuario():
    try:
        id_usuario = int(input("Digite o ID do usuário: "))

        if verificar_emprestimos_ativos(id_usuario=id_usuario):
            print('Usuário possui empréstimos ativos e não pode ser excluído.')
            return

        deletados = deletar_usuario(id_usuario)

        if deletados > 0:
            print('Usuário deletado com sucesso.')
        else:
            print('Nenhum usuário encontrado com esse ID.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def atualizar_usuario():
    try:
        from menus.menu_usuarios import menu_update_usuarios

        id_usuario = int(input("Digite o ID do usuário que deseja atualizar: "))
        usuario = buscar_usuario(id_usuario)

        if not usuario:
            print("Usuário não encontrado.")
            return
        
        while True:
            opcao = menu_update_usuarios()
            
            match opcao:

                case "0":
                    break

                case "1":
                    novo_nome = input("Digite o novo nome: ").strip()
                    if novo_nome:
                        if atualizar_usuario_db(id_usuario, "nome", novo_nome):
                            print("Nome atualizado com sucesso!")
                    else:
                        print("Nome não pode ser vazio.")
                case "2":
                    novo_sobrenome = input("Digite o novo sobrenome: ").strip()
                    if novo_sobrenome:
                        if atualizar_usuario_db(id_usuario, "sobrenome", novo_sobrenome):
                            print("Sobrenome atualizado com sucesso!")
                    else:
                        print("Sobrenome não pode ser vazio.")
                case "3":
                    nova_data = validar_data(input("Digite a nova data de nascimento (AAAA-MM-DD): "))
                    if nova_data:
                        if atualizar_usuario_db(id_usuario, "data_nascimento", nova_data):
                            print("Data de nascimento atualizada com sucesso!")
                    else:
                        print("Digite uma data válida. (AAAA-MM-DD)")
                case _:
                    print("Opção inválida, tente novamente.")

    except ValueError:
        print("ID inválido, digite um número.")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
                
def cadastrar_usuario():
    try:    
        print("\n--- CADASTRAR USUÁRIO ---")
        nome = input("Nome do usuário: ")
        sobrenome = input("Sobrenome do usuário: ")
        data_nascimento = validar_data(input("Data de nascimento do usuário (ano-mes-dia): "))

        cadastrar_usuario_db(nome, sobrenome, data_nascimento)
        print("Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro inesperado: {e}")
