"""Crie uma lista (de 4 ou mais elementos) e um programa que permita ao usuário acessar os elementos desta lista.
O usuário deve inserir um índice (número inteiro) para obter o elemento correspondente na lista.
Trate casos em que o índice inserido está fora do intervalo da lista ou se o usuário inserir algo que não seja um número
(Dica: ‘try’, ‘except’). Se ocorrer um erro, informe ao usuário qual o erro e permita que ele tente novamente."""

lista = ["elemento 1","elemento 2","elemento 3","elemento 4","elemento 5",]
print(lista)

while True:
    try:
        indice = int(input(f"Digite um índice entre 0 e {len(lista) - 1}: "))
        print(lista[indice])
        break

    except IndexError:
        print("Erro: Índice fora do Intervalo da lista.")

    except ValueError:
        print('Erro: Digite um número válido.')