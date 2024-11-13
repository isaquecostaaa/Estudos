def retorna_pares(L):
    pares = []
    for i in L:
        if i % 2 == 0:
            pares.append(i)
    return pares

L2 = [5,6,8,10,13,15]

nova_L2 = retorna_pares(L2)
print(nova_L2)

#===================================

string = 'abacate, alface, tomate, milho'
novo_string = string.split(",")
print(novo_string)

def custom_split(texto):
    lista = []
    k = 0
    for i, c in enumerate(texto):
        if c == ',':
            lista.append(texto[k:i])
            k = i + 1
    lista.append(texto[k:])
    return lista

def descreve_pessoa(nome, sobrenome, idade=None, linguagem_favorita="C++"):
    print('nome:', nome)
    print('Sobrenome:', sobrenome)
    print('Idade:', idade)
    print('Linguagem favorita:', linguagem_favorita)

print(descreve_pessoa(nome="isaque", sobrenome="Costa"))

def soma1(num1, num2):
    return num1 + num2

print(soma1(3,6))

def soma2(*nums):
    return sum(nums)

print(soma2(3,6,7))

def soma3(num1, num2, *nums):
    return num1 + num2 + sum(nums)

print(soma3(num1=2, num2=7))

# ===============================

def funcao_pop (li, i=None):
    if i is not None and i < len(li):
        del li[i]
        return li
    else:
        del li[-1]
        return li

print(funcao_pop(li=['1','2','3'],i=1))

def my_enumerate(lista):
    idx = 0
    resultado = []
    for item in lista:
        resultado.append((idx, item))
        idx += 1
    return resultado



