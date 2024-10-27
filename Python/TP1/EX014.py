"""Escreva um programa que permita ao usuário votar em três opções diferentes
e, no final, exiba o número de votos de cada opção."""

votos_opcao1 = 0
votos_opcao2 = 0
votos_opcao3 = 0

print("Opções de voto:")
print("1 - opção 1")
print("2 - opção 2")
print("3 - opção 3")
print("0 - Encerrar")

while True :
    user_input = int(input("Digite a opção desejada: "))
    if user_input == 1 :
        votos_opcao1 += 1
    elif user_input == 2 :
        votos_opcao2 += 1
    elif user_input == 3 :
        votos_opcao3 += 1
    elif user_input == 0 :
        break
    else :
        print("Digite uma opção válida.")

print("\nResultado da votação:")
print(f"Opção 1: {votos_opcao1} votos")
print(f"Opção 2: {votos_opcao2} votos")
print(f"Opção 3: {votos_opcao3} votos")