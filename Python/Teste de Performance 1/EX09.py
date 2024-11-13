"""Desenvolva um programa que aplique descontos progressivos com base no valor da compra:
desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500,
para valores maiores do que esse, o desconto é fixado em 25%."""

preco = int(input("Digite o preço: "))

if preco > 100 :
    desconto = preco - (preco * 0.10)
    print(f"Desconto de 10% aplicado: R${desconto}")
elif preco > 200 :
    desconto = preco - (preco * 0.15)
    print(f"Desconto de 15% aplicado: R${desconto}")
elif preco > 300 :
    desconto = preco - (preco * 0.20)
    print(f"Desconto de 20% aplicado: R${desconto}")
elif preco > 400 :
    desconto = preco - (preco * 0.25)
    print(f"Desconto de 25% aplicado: R${desconto}")
else :
    print("Desconto não disponível neste valor.")