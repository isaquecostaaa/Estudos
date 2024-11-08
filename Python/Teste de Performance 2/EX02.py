"""Crie duas tuplas e verifique se elas possuem os mesmos elementos,
independente da ordem (Ex: tupla1 = (1,3,5) e tupla2 = (5, 1, 3) possuem SIM os mesmos elementos)."""

tupla1 = ("Isaque","Silva","Costa")
tupla2 = ("Silva", "Costa", "Isaque")

def verifica_elementos1(tupla1, tupla2):
    """Verificação usando a função sorted"""

    if sorted(tupla1) == sorted(tupla2):
        return "Possui os mesmos itens"

    return "Não possui os mesmos itens"

def verifica_elementos2(tupla1, tupla2):
    """verificação usando for"""

    for item in tupla1:
        if item not in tupla2:
            return "Não possui os mesmos itens"

    for item in tupla2:
        if item not in tupla1:
            return "Não possui os mesmos itens"

    return "Possui os mesmos itens"

print(verifica_elementos1(tupla1, tupla2))
print(verifica_elementos2(tupla1, tupla2))