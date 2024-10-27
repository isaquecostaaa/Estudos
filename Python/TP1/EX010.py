"""Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais)
para criar uma história curiosa."""

import random

personagens = ["O Superman","O Batman","A Mulher-Maravilha","O Homem-Aranha"]
acoes = ["salvou o dia","ajudou uma idosa","fez uma acrobacia","derrotou um vilão"]
locais = ["em um shopping!","em um trem!","no avião!","em um hospital!"]

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

print(f"Um dia, {personagem} {acao} {local}")