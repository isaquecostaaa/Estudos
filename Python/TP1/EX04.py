operacao = input("Digite a operação desejada: (adição, subtração, divisão, multiplicação) ")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if operacao == "adição" :
    print(f"A soma é {num1 + num2}")
elif operacao == "subtração" :
    print(f"A subtração é {num1 - num2}")
elif operacao == "divisão" :
    print(f"A divisão é {num1 / num2}")
elif operacao == "multiplicação" :
    print(f"A multipicação é {num1 * num2}")
else :
    print("operação não reconhecida.")

""" algumas vezes a IDE não reconhece a operação mesmo quando digitada corretamente,
caso isso aconteça dê run novamente """