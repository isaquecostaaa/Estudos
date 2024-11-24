#%%

# 1)

print(list(map(lambda numero: numero ** 2, map(int, input("Digite uma lista de números separados por espaço: ").split()))))

#%%

# 2)

print(list(map(lambda numero: 0 if numero < 10 else numero, map(int, input("Digite uma lista de números separados por espaço: ").split()))))

#%%

# 3)

print([len(frase.split()) for frase in input("Conte uma história (use pontos para separar as frases): ").split('.') if frase.strip()])

#%%

# 4)

print([sum(1 for vogal in frase if vogal.lower() in 'aáâãeéêiíîoóôuúû') for frase in ["Odeio programar", "Está chovendo", "Hoje é sábado"]])

#%%

# 5)

def filtrar_maiores_idade(idades):
    """
    Cria um dicionário com pessoas maiores de idade a partir de um dicionário de idades.

        idades (dict): Dicionário com nomes como chaves e idades como valores.

        dict: Dicionário contendo apenas pessoas com 18 anos ou mais.
    """
    return {pessoa: idade for pessoa, idade in idades.items() if idade >= 18}

idades_geral = {"João": 25, "Maria": 30, "Pedro": 22, "Ana": 28, "Lucas": 17, "Sophia": 16}
print(filtrar_maiores_idade(idades_geral))

#%%

# 6)

def remover_palavras_indesejadas(frase, palavras_indesejadas):
    """
    Remove palavras indesejadas de uma string.

        frase: String original.
        palavras_indesejadas: Lista de palavras que devem ser removidas.
    """
    palavras = frase.split()
    palavras_filtradas = [palavra for palavra in palavras if palavra not in palavras_indesejadas]
    return ' '.join(palavras_filtradas)

print(remover_palavras_indesejadas("eu não gosto muito de programar em python", ["não", "muito"]))

#%%

# 7)

def alternar_maiusculo_minusculo(texto):
    """
    Alterna entre letras maiúsculas e minúsculas em uma string, começando com maiúscula.

        texto: Texto original.
    """
    novo_texto = ""
    for i, letra in enumerate(texto):
        if i % 2 == 0:
            novo_texto += letra.upper()
        else:
            novo_texto += letra.lower()
    return novo_texto

print(alternar_maiusculo_minusculo("desenvolvendo habilidades"))

#%%

# 8)

def identificar_unicos(listas):
    """
    Retorna uma lista de elementos únicos a partir de uma lista de listas.

    Args:
        listas: Lista contendo outras listas.

    Returns:
        list: Lista de elementos únicos.
    """
    unicos = set()
    for lista in listas:
        unicos.update(lista)
    return list(unicos)

print(identificar_unicos([[2, 4, 6], [4, 5, 1, 6], [2, 2, 6]]))

#%%

# 9)

def intercalar_listas(primeira_lista, segunda_lista):
    """
    Intercala os elementos de duas listas em uma string.

    Returns:
        String com palavras intercaladas e restantes.
    """
    intercalada = []
    max_len = max(len(primeira_lista), len(segunda_lista))
    for i in range(max_len):
        if i < len(primeira_lista):
            intercalada.append(primeira_lista[i])
        if i < len(segunda_lista):
            intercalada.append(segunda_lista[i])
    return " ".join(intercalada)

print(intercalar_listas(["eu", "muito"], ["amo", "programar"]))

#%%

# 10)

def verificar_tamanho(lista, minimo):
    """
    Separa uma lista de palavras em duas listas: palavras com comprimento menor ou igual a n e maior que n.

        lista: Lista de palavras.
        minimo: Comprimento mínimo de separação.

    Returns:
        Lista contendo duas listas: palavras menores/iguais a n e palavras maiores que n.
    """
    menores = []
    maiores = []
    for item in lista:
        if len(item) <= minimo:
            menores.append(item)
        else:
            maiores.append(item)
    return [menores, maiores]

palavras_separadas = verificar_tamanho(["ola", "mundo", "da", "programação"], 5)
print(palavras_separadas)

#%%

# 11)

def inserir_palavra(lista, nova_palavra):
    """
    Insere uma nova palavra em uma lista em uma posição definida pelo usuário.
    Se a lista tiver menos de 3 elementos, a palavra é adicionada automaticamente no final.

        lista: Lista inicial de palavras.
        nova_palavra: Palavra a ser inserida.

    Returns:
        Lista atualizada com a nova palavra.
    """
    if len(lista) < 3:
        lista.append(nova_palavra)
        print(f"Lista com menos de 3 elementos. '{nova_palavra}' foi adicionada ao final da lista.")
    else:
        while True:
            try:
                posicao = int(input(f"Informe a posição para inserir '{nova_palavra}' (0 a {len(lista)}): "))
                if 0 <= posicao <= len(lista):
                    lista.insert(posicao, nova_palavra)
                    break
                else:
                    print(f"Posição inválida. Insira um número entre 0 e {len(lista)}.")
            except ValueError:
                print("Por favor, insira um número válido.")
    return lista

lista_de_palavras = ["casa", "carro", "bicicleta"]
nova_palavra = "avião"
lista_de_palavras = inserir_palavra(lista_de_palavras, nova_palavra)
print("Lista atualizada:", lista_de_palavras)

#%%

# 12)

def combinar_listas(lista1, lista2):
    """
    Combina duas listas de números em uma única lista usando extend

        lista1: Primeira lista de números.
        lista2: Segunda lista de números.

    Returns:
        Lista combinada.
    """
    lista1.extend(lista2)
    return lista1

lista_extendida = combinar_listas([1, 2, 3], [4, 5, 6])
print(lista_extendida)

#%%

# 13)

def remover_duplicatas(lista):
    """
    Remove todas as ocorrências de palavras duplicadas de uma lista, mantendo apenas a primeira ocorrência.

        lista: Lista de palavras.

    Returns:
        Lista sem duplicatas.
    """
    lista_unica = []
    for palavra in lista:
        if palavra not in lista_unica:
            lista_unica.append(palavra)
    return lista_unica

print(remover_duplicatas(["mundo", "olá", "olá", "mundo"]))

#%%

# 14)

def gerenciar_compras(lista_compras):
    """
    Remove o último item de uma lista de compras, simulando o cancelamento da última compra.
    Informa se a lista estiver vazia.

        lista_compras: Lista de itens de compras.

    Returns:
        Lista atualizada de compras.
    """
    if lista_compras:
        removido = lista_compras.pop()
        print(f"Item '{removido}' foi removido.")
    else:
        print("A lista de compras está vazia. Nenhum item para remover.")
    print("Lista de compras atualizada:", lista_compras)
    return lista_compras

compras = ["Arroz", "Feijão", "Macarrão"]
compras = gerenciar_compras(compras)

#%%

# 15)

def manipular_string(string):
    """
    Exibe uma substring de uma string com base em índices fornecidos pelo usuário.

        string: String original.
    """
    print(f"String original: {string}")
    try:
        inicio = int(input("Digite o índice de início da substring: "))
        fim = int(input("Digite o índice de fim da substring: "))
        if 0 <= inicio < len(string) and 0 < fim <= len(string) and inicio < fim:
            print(f"Substring correspondente: {string[inicio:fim]}")
        else:
            print("Índices inválidos.")
    except ValueError:
        print("Por favor, insira índices válidos.")

manipular_string("Python é incrível!")

#%%

# 16)

def gerenciar_lista_compras(lista_compras):
    """
    Gerencia uma lista de compras com operações de adicionar, remover e encerrar.

        lista_compras: Lista inicial de compras.

    Returns:
        Lista de compras atualizada após as operações.
    """
    while True:
        print("\nLista de compras atual:", lista_compras)
        comando = input("Digite um comando:\n 'adicionar [índice] [item]'\n 'remover [item/índice]'\n 'fim' para encerrar: ").strip()

        if comando.lower() == "fim":
            print("Encerrando o gerenciador de lista de compras.")
            break

        if comando.startswith("adicionar"):
            try:
                _, indice, item = comando.split(maxsplit=2)
                indice = int(indice)
                if 0 <= indice <= len(lista_compras):
                    lista_compras.insert(indice, item)
                    print(f"Item '{item}' adicionado na posição {indice}.")
                else:
                    print("Índice inválido.")
            except (ValueError, IndexError):
                print("Comando inválido. Use: 'adicionar [índice] [item]'.")

        elif comando.startswith("remover"):
            try:
                _, argumento = comando.split(maxsplit=1)
                if argumento.isdigit():
                    indice = int(argumento)
                    if 0 <= indice < len(lista_compras):
                        removido = lista_compras.pop(indice)
                        print(f"Item '{removido}' removido.")
                    else:
                        print("Índice inválido.")
                else:
                    if argumento in lista_compras:
                        lista_compras.remove(argumento)
                        print(f"Item '{argumento}' removido.")
                    else:
                        print("Item não encontrado na lista.")
            except ValueError:
                print("Comando inválido. Use: remover [item/índice].")

        else:
            print("Comando não reconhecido.")

    print("\nLista final de compras:", lista_compras)
    return lista_compras

lista_de_compras = ["Arroz", "Feijão", "Macarrão"]
lista_de_compras = gerenciar_lista_compras(lista_de_compras)
