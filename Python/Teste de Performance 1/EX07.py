"""Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça
feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso)"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc > 18.5 and imc <= 24.9:
    print("Você está com peso normal.")
elif imc > 25:
    print("Você está com sobrepeso.")
