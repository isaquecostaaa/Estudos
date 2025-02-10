#%%
# 1)

def somar_valores(lista):
    return sum(lista)

lista = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
print(somar_valores(lista))

#%%
# 2)
def remover_duplicatas(lista):

    lista_sem_duplicatas = []
    itens_vistos = set()

    for item in lista:
        if item not in itens_vistos:
            lista_sem_duplicatas.append(item)
            itens_vistos.add(item)

    return lista_sem_duplicatas

lista = [5,3,1,4,5,3,4,3,2,1,4,5]
print(remover_duplicatas(lista))

#%%
# 3)
def ordenar_idade(lista):

    return sorted(lista,key=lambda x: x[1])

lista_tuplas = [
    ("João", 25),
    ("Maria", 30),
    ("Pedro", 22),
    ("Ana", 28),
    ("Carlos", 35)
]
print(ordenar_idade(lista_tuplas))

#%%
# 4)
def contar_palavras(texto):
    contagem_palavras = {}
    palavras = texto.split()

    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    return contagem_palavras

string = "sol sol sol lua lua lua lua estrela estrela estrela estrela estrela mar mar mar mar mar céu céu céu céu céu céu"
print(contar_palavras(string))

#%%
# 5)
def inverter_chaves(dict):
    novo_dicionario = {valor: chave for chave, valor in dict.items()}
    return novo_dicionario

dicionario_original = {"a": 1, "b": 2, "c": 3}
print(inverter_chaves(dicionario_original))

#%%
# 6)
def juntar_dicionarios(dict_1, dict_2):
    novo_dicionario = {}

    for chave, valor in dict_1.items():
        novo_dicionario[chave] = valor

    for chave, valor in dict_2.items():
        if chave in novo_dicionario:
            novo_dicionario[chave] += valor
        else:
            novo_dicionario[chave] = valor
        
    return novo_dicionario
    
dict_1 = {"item_a": 1, "item_b": 2,"item_c": 3,"item_d": 4,"item_e": 5, }
dict_2 = {"item_e": 6, "item_f": 7,"item_g": 8,"item_h": 9,"item_i": 10, }
print(juntar_dicionarios(dict_1, dict_2))

#%%
# 7)
def manipulação_de_conjuntos(conjunto1, conjunto2):
        return {
        "união": conjunto1 | conjunto2,
        "interseção": conjunto1 & conjunto2,
        "diferença": conjunto1 - conjunto2
    }

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
print(manipulação_de_conjuntos(conjunto1, conjunto2))

# %%
# 6)
def encontrar_unicos(lista):
    return list(dict.fromkeys(lista))


lista = [1, 2, 2, 3, 3, 4, 4, 5, 5]
print(encontrar_unicos(lista))

# %%
# 9)
def verificar_subconjuntos(conjunto1, conjunto2):

    if conjunto1.issubset(conjunto2):
        return True
    elif conjunto2.issubset(conjunto1):
        return True
    else:
        return False
    
conjunto1 = {1,2,3,4}
conjunto2 = {1,2}
print(verificar_subconjuntos(conjunto1, conjunto2))

# %%
# 10)
import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, newline='', mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                print(linha)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

ler_csv("dados.csv")
# %%
# 11)
import csv

def escrever_csv(nome_arquivo, dados):
    if not dados:
        print("Nenhum dado para escrever.")
        return

    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' foi criado com sucesso!")

dados = [
    {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Pedro", "Idade": 22, "Cidade": "Belo Horizonte"}
]

escrever_csv('exemplo.csv', dados)

# %%
# 12)
import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as file:
            dados = json.load(file)
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o conteúdo do arquivo '{nome_arquivo}'. Verifique se o arquivo contém um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

dados = ler_json('dados2.json')
if dados:
    print(dados)

# %%
# 13)
import json

def salvar_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', encoding='utf-8') as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
dados = {
    "clientes": [
        {"nome": "João", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Pedro", "idade": 22, "cidade": "Belo Horizonte"}
    ]
}

salvar_json('clientes.json', dados)

# %%
# 14)
import csv

def agrupar_por_cidade(nome_arquivo):
    cidades = {}

    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            
            for linha in leitor:
                nome = linha['nome']
                cidade = linha['cidade']
                
                if cidade not in cidades:
                    cidades[cidade] = []
    
                cidades[cidade].append(nome)

        return cidades
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

cidades = agrupar_por_cidade('pessoas.csv')
if cidades:
    print(cidades)


# %%
# 15)
def nomes_unicos(arquivo):
    with open(arquivo, 'r') as f:
        nomes = f.readlines()

    return set(nome.strip() for nome in nomes)

nomes = nomes_unicos('nomes.txt')
print(nomes)

# %%
# 16)
def palavras_por_linha(arquivo):
    dicionario = {}
    
    with open(arquivo, 'r') as f:
        for numero_linha, linha in enumerate(f, 1):
            palavras = linha.split()
            
            for palavra in palavras:
                palavra = palavra.strip('.,!?";:()[]{}').lower()
                
                if palavra in dicionario:
                    dicionario[palavra].add(numero_linha)
                else:
                    dicionario[palavra] = {numero_linha}
    
    return dicionario

dicionario = palavras_por_linha('texto.txt')
print(dicionario)

# %%
