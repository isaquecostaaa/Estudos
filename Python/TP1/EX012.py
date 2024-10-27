"""Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras)
ou longas (5 letras ou mais)"""

palavras = input("Digite as palavras separadas por espaço: ").split()

curtas = []
longas = []

for palavra in palavras :
    if len(palavra) < 5 :
        curtas.append(palavra)

    else :
        longas.append(palavra)

print(f"palavras curtas: {curtas}")
print(f"palavras longas: {longas}")
