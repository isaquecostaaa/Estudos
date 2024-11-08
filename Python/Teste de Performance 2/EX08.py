"""Número Mágico: Crie um código para adivinhar um número aleatório entre 1 e 20 com um limite de 4 tentativas
(ou seja, o programa recebe essas tentativas do usuário e verifica se o número que o usuário escreveu é o número mágico).
OBS: Para cada número digitado, informe se ele está abaixo ou acima do número mágico."""

from random import randint

def verificar_palpite():
    numero_aleatorio = randint(1, 20)
    chances = 4

    print("NÚMERO ALEATÓRIO DE 1 A 20 GERADO!!")

    while chances > 0:
        try:
            palpite = int(input("Qual é o seu palpite? "))

            if palpite == numero_aleatorio:
                print(f"Você acertou! O número é {numero_aleatorio}")
                break

            if 1 <= palpite <= 20:
                chances -= 1
                if palpite > numero_aleatorio:
                    print(f"Você errou! Seu palpite está acima do número mágico. Resta(m) {chances} tentativa(s).")
                else:
                    print(f"Você errou! Seu palpite está abaixo do número mágico. Resta(m) {chances} tentativa(s).")
            else:
                print("Número inválido, digite um número entre 1 e 20.")

        except ValueError:
            print("Digite um número válido.")

    else:
        print(f"Você perdeu! O número era {numero_aleatorio}")

verificar_palpite()





