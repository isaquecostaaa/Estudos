"""Crie uma lista (maior que 5 elementos) e encontre os dois números cuja soma seja o mais próximo possível de zero."""

lista = [-1,1,2,4,3,5,4,5,6]

def verificar_proximos_zero(lista):
    lista.sort()
    soma_proxima = float('inf')
    numeros_proximos = (None, None)

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            soma_atual = lista[i] + lista[j]
            if abs(soma_atual) < abs(soma_proxima):
                soma_proxima = soma_atual
                numeros_proximos = (lista[i], lista[j])

    return numeros_proximos

print(verificar_proximos_zero(lista))


