"""Escreva um programa onde o usuário deve adivinhar um número secreto.
O programa deve dizer se o palpite está correto, muito alto ou muito baixo."""

import random

randomNum = int(random.random() * 100)
palpite = 0

while True:
    palpite = int(input("Digite um palpite de 1 a 100: "))

    if palpite > randomNum:
        print("Seu palpite está alto! \n")
    elif palpite < randomNum:
        print("Seu palpite está baixo!\n")
    elif palpite == randomNum:
        print(f"Você acertou! o número é {randomNum}\n")
        break