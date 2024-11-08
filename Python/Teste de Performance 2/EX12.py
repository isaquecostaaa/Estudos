"""Joel possui uma barraca na feira e quer dar um presente a um cliente. Crie um programa que receba do usuário uma
lista de frutas disponíveis na barraca e as quantidades correspondentes de cada fruta. O programa deve escolher
aleatoriamente uma fruta para presentear o cliente. Se o número de quantidades fornecido for maior do que o número
de frutas, o programa deve contabilizar apenas até o último índice da lista de frutas. Caso o número de quantidades
seja menor do que o número de frutas, o programa deve solicitar ao usuário que reescreva a lista de quantidades
(Ex: input do usuário: ‘maçã, banana, laranja’ | ‘10, 5, 8’)."""

import random
def escolher_presente():

    while True:
        frutas = input("Digite as frutas disponíveis separadas por vírgula: ").split(", ")
        quantidades = input("Digite as quantidades correspondentes para cada fruta, separadas por vírgula: ").split(", ")

        try:
            quantidades = [int(q) for q in quantidades]
        except ValueError:
            print("Por favor, insira apenas números inteiros para as quantidades.")
            continue

        if len(frutas) > len(quantidades):
            frutas = frutas[:len(quantidades)]
            break
        elif len(frutas) < len(quantidades):
            print("O número de quantidades é maior que o número de frutas. Por favor, reescreva as listas.")
            continue
        else:
            break

    fruta_presenteada = random.choice(frutas)
    print(f"Presente para o cliente: {fruta_presenteada}")

escolher_presente()
