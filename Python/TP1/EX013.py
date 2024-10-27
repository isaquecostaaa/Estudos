"""Desenvolva um programa que verifique se uma palavra
ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente)."""

user_input = input("Digite uma palvra ou uma frase: ")

cleaned_input = user_input.replace(" ", "").lower()
reversed_input = ""

for char in cleaned_input :
    reversed_input = char + reversed_input


print(f"A string revertida é: '{reversed_input}'")
if reversed_input == cleaned_input :
    print("O texto é um palindromo")
else :
    print("O texto não é um palíndromo")