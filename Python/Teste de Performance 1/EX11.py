"""Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar
e o programa deve exibir os resultados."""

import random

quantidade_dados = int(input("Digite a quantidade de dados: "))

if quantidade_dados > 0 :
    resultados = []
    for i in range(quantidade_dados):
        resultado = random.randint(1,6)
        resultados.append(resultado)

        print(f"{i + 1}º Dado: {resultado}")

else :
    print("Digite um valor positivo de dados.")




