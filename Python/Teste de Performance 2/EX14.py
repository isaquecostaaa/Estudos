"""Defina uma função chamada ‘dividir’ que recebe dois números e retorna dois outputs: o resultado inteiro da divisão
e o resto. Escreva uma docstring para documentar o que a função faz, quais são seus parâmetros, e o que ela retorna."""

def dividir(dividendo, divisor):
    """
    Realiza a divisão entre dois números e retorna o resultado inteiro e o resto

    parâmetros:
    dividendo: O número a ser dividido
    divisor: o número pelo qual o dividendo será dividido

    retorno: retorna os valores de cada operação
    """

    if divisor == 0:
        print("Erro: não é possível dividir por 0")
        return

    return dividendo //divisor, dividendo % divisor

inteiro, resto = dividir(10, 3)
print(f"Resultado inteiro: {inteiro}, Resto: {resto}")