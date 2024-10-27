"""Crie um programa que apresente ao usuário uma série de escolhas (como em uma história)
e conduza a diferentes resultados com base nessas escolhas."""

opcao_invalida = "Digite uma opção válida"
separador = "=============================="

print("Durante uma busca por suprimentos, você encontrou um hospital abandonado.")
print("O que você faz?")
print("1 - Entrar no hospital.")
print("2 - Seguir em frente.")

escolha1 = int(input("Digite o número de sua escolha: "))

if escolha1 == 1 :
    print(separador)
    print("Ao entrar, percebe que tudo parece ter sido abandonado as pressas, deixando tudo para trás.")
    print("Há uma escada para o segundo andar e um corredor. \nO que você faz?")
    print("1 - Sai do Hospital e segue em frente.")
    print("2 - Sobe a escada.")
    print("3 - Segue no corredor.")

    escolha2 = int(input("Digite o número de sua escolha: "))

    if escolha2 == 1 :
        print(separador)
        print("Você não encontrou mais nada a frente e voltou ao seu abrigo.")
    elif escolha2 == 2 :
        print(separador)
        print("Você sobe a escada e encontra equipamentos de primeiros socorros.")
        print("Com a noite chegando, você decide voltar ao seu abrigo.")
    elif escolha2 == 3 :
        print(separador)
        print("Você segue no corredor e vê dois caminhos diferentes:")
        print("1 - Uma porta entreaberta")
        print("2 - Uma escadaria para o andar debaixo")

        escolha3 = int(input("Por onde você vai? "))

        if escolha3 == 1 :
            print(separador)
            print("Você encontrou a cozinha. Ainda há alguns alimentos.")
            print("Você pega o que consegue carregar e volta ao abrigo.")

        elif escolha3 == 2 :
            print(separador)
            print("Ao descer você encontra um zumbi, que te ataca!")
            print("GAME OVER")
        else:
            print(separador)
            print(opcao_invalida)


    else :
        print(separador)
        print(opcao_invalida)

elif escolha1 == 2 :
    print(separador)
    print("Você não encontrou mais nada a frente e voltou ao seu abrigo.")

else :
    print(separador)
    print(opcao_invalida)