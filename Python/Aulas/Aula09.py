lista = [50, 4, 77, 60, 10 ,12]

lista_impares = list(filter(lambda numero: numero % 2 != 0, lista))
print(lista_impares)

def eh_par(numero):
    return numero % 2 == 0

def processar_numero(numero):
    numero_dobrado = numero * 2

    if eh_par(numero):
        print(f"O numero {numero} é par")
        return numero_dobrado
    else:
        print(f"O número {numero} é impar")
        return False

num = 54
print(processar_numero(num))

def contar_caracteres(texto):
    return len(texto)

def contar_palavras_unicas(texto):
    palavras = texto.split()
    return len(set(palavras))

def analisar_texto(texto):
    total_caracteres = contar_caracteres(texto)
    total_palavras_unicas = contar_palavras_unicas(texto)
    return f"tem {total_caracteres} caracteres e {total_palavras_unicas} palavras"

exemplo = "este é um exemplo de palavras repetidas repetidas"
print(analisar_texto(exemplo))

"""
def funcao1(*params):

def funcao2(*params):


def main():
    funcao1()
    funcao2()
"""

def verificar_media(numeros):
    total_numeros = sum(numeros)
    return total_numeros / len(numeros)

def verificar_maximo(numeros):
    maior_valor = max(numeros) if numeros else None
    return maior_valor

def main(numeros, limite_media, limite_maximo):
    media = verificar_media(numeros)
    maximo = verificar_maximo(numeros)

    if media > limite_media and maximo > limite_maximo:
        print("Ambos media e maximo ultrapassam")
        return

    if media > limite_media:
        print("A média ultrapassa o limite")
    else:
        print("A media está dentro do limite")

    if maximo > limite_maximo:
        print("O maximo ultrapassa o limite")
    else:
        print("O maximo está dentro do limite")


lista = [10, 25, 30, 45, 60]

main(lista, 40, 59)


def transformar_minusculo(texto):
    return texto.lower()

def contar_caracteres(texto):
    return len(texto)

def primeira_palavra(texto):
    texto_dividido = texto.split()
    return texto_dividido[0]

def funcao_principal(texto):
    # texto_minusculo = transformar_minusculo(texto)
    # total_caracteres = contar_caracteres(texto)
    # primeira = primeira_palavra(texto)
    #
    # return {'texto_minusculo': texto_minusculo, 'total_caracteres': total_caracteres, 'primeira_palavra': primeira}
    return {'texto_minusculo': transformar_minusculo(texto), 'total_caracteres': contar_caracteres(texto), 'primeira_palavra': primeira_palavra(texto)}

print(funcao_principal("ISAQUE É LINDIO"))

def calcula_soma(numeros):
    return sum(numeros)

def menor_valor(numeros):
    return min(numeros)

def dobrar_numeros(numeros):
    return list(map(lambda numero: numero * 2, numeros))

def op_numeros(numeros):
    soma = calcula_soma(numeros)
    menor = menor_valor(numeros)
    dobrar = dobrar_numeros(numeros)

    return {'soma': soma, 'menor_valor': menor, 'valores_dobrados':dobrar}

print(op_numeros([1,2,3,4,5,6,7,8,9]))