"""Defina uma função que receba um nome e uma idade como argumentos obrigatórios e uma cidade como argumento opcional
(valor padrão "Desconhecida"). A função deve imprimir uma mensagem personalizada com essas informações.
Ex: "Maria tem 30 anos e mora em São Paulo"."""

def criar_mensagem(nome,idade, cidade="Desconhecida"):
    if cidade != "Desconhecida":
        return f"{nome} tem {idade} anos e mora em {cidade}"
    return f"{nome} tem {idade} anos e a cidade é {cidade}"

print(criar_mensagem("Isaque", 20,"Rio de Janeiro"))
print(criar_mensagem("Isaque", 20,))