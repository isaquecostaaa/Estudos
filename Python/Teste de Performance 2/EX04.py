"""Crie dois dicionários (com 2 ou mais elementos) e verifique se um é subconjunto de outro."""

primeiro_dicionario = {'1':1, '2':2,'3':3}
segundo_dicionario = {'1':1, '2':2}

def verificar_subconjuntos(dict1, dict2):

    return all(item in dict2.items() for item in dict1.items())

print("O Segundo é subconjunto do primeiro?",verificar_subconjuntos(segundo_dicionario, primeiro_dicionario))
print("O primeiro é subconjunto de Segundo?",verificar_subconjuntos(primeiro_dicionario,segundo_dicionario))
