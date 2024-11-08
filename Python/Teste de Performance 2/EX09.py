"""Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo.
OBS: Non-case sensitive e sem contar os espaços (Ex: "A mala nada na lama" é um palíndromo)."""

def verificar_palindromo():
    palavra = input("Digite uma palavra ou frase: ")

    palavra_formatada = palavra.replace(" ","").lower()
    palindromo = palavra_formatada[::-1]

    if palindromo == palavra_formatada:
        print(f'"{palavra}" é um palíndromo')
        return True
    else:
        print(f'"{palavra}" não é um palíndromo')
        return False

verificar_palindromo()
