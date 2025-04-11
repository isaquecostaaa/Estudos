from datetime import datetime
from src.utils.validar_data import validar_data
from src.crud.emprestimos_db import *
from src.crud.livros_db import verificar_livro_existente, diminuir_disponibilidade, aumentar_disponibilidade
from src.crud.usuarios_db import verificar_usuarios_existente

def consultar_emprestimos():
    try:
        emprestimos = buscar_emprestimos()

        if emprestimos:
            print("-- EMPRÉSTIMOS --")
            print("-" * 40)
            for emprestimo in emprestimos:
                id_emprestimo, id_livro, id_usuario, data_emprestimo, data_devolucao = emprestimo
                resultado = buscar_usuarios_emprestimos(id_livro, id_usuario)

                if resultado:
                    titulo, nome, sobrenome = resultado

                    print(f"ID do empréstimo: {id_emprestimo}")
                    print(f"Nome: {nome} {sobrenome}")
                    print(f"Livro: {titulo}")
                    print(f"Data do empréstimo: {data_emprestimo}")
                    if data_devolucao:
                        print(f"Data de devolução: {data_devolucao}")
                    else:
                        print("Livro ainda não devolvido.")
                    print("-" * 40)
        else:
            print("Não há empréstimos registrados.")
    except Exception as e:
        print(f"Erro ao consultar empréstimos: {e}")

def realizar_emprestimo():
    try:
        print("\n--- REALIZAR EMPRÉSTIMO ---")
        id_usuario = int(input("ID do usuário: "))
        id_livro = int(input("ID do livro: "))
        
        usuario_existe = verificar_usuarios_existente(id_usuario)
        if not usuario_existe:
            print("Usuário não encontrado.")
            return

        livro = verificar_livro_existente(id_livro)
        if not livro:
            print("Livro não encontrado.")
            return
        
        disponivel = livro[0]
        if disponivel < 1:
            print("Livro não disponível para empréstimo.")
            return

        emprestimos_ativos = verificar_emprestimos_ativos(id_usuario=id_usuario)
        if emprestimos_ativos >= 5:
            print("Usuário já tem 5 empréstimos ativos. Limite atingido.")
            return

        inserir_emprestimo(id_livro, id_usuario)
        
        diminuir_disponibilidade(id_livro)
        print("Empréstimo realizado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

def atualizar_emprestimo():
    try:
        from menus.menu_emprestimos import menu_update_emprestimos

        id_emprestimo = int(input("Digite o ID do empréstimo: "))

        while True:
            opcao = menu_update_emprestimos()
            match opcao:
                case "1":
                    nova_data = validar_data(input("Digite a nova data do empréstimo:"))
                    if nova_data:
                        atualizar_emprestimo_db(id_emprestimo, "data_emprestimo", nova_data)
                    print("Data de empréstimo atualizada com sucesso!")
                
                case "2":    
                    emprestimo_ativo = verificar_emprestimos_ativos()

                    if not emprestimo_ativo:
                        print("Nenhum empréstimo ativo encontrado com esse ID.")
                        return

                    id_livro = emprestimo_ativo[0]
                    data_hoje = datetime.now().strftime('%Y-%m-%d')

                    atualizar_emprestimo_db(id_emprestimo, "data_devolucao", data_hoje)
                    aumentar_disponibilidade(id_livro)

                    print('Livro devolvido com sucesso.')
                case "0":
                    break
                case _:
                    print("Digite uma opção válida.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def excluir_emprestimo():
    try:
        id_emprestimo = int(input("Digite o ID do empréstimo: "))

        emprestimo = buscar_emprestimo(id_emprestimo)

        if not emprestimo:
            print('Nenhum empréstimo encontrado com esse ID.')
            return

        id_emprestimo, data_devolucao = emprestimo

        if data_devolucao is None:
            print(f"Aviso: empréstimo de ID:{id_emprestimo} ainda está ativo, não é possível excluí-lo.")
            return
        
        excluir_emprestimo_db(id_emprestimo)
        print('Empréstimo deletado com sucesso.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
