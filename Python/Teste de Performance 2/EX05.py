"""Crie um dicionário que mapeia alunos e suas notas e retorne um novo dicionário que classifique os alunos em
"Aprovado" (nota >= 7) e "Reprovado" caso contrário (Ex: notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}
deve retornar {'Aprovado': ['Ana', 'Maria'], 'Reprovado': ['Pedro', 'José']})."""

notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}

def verificar_aprovacao(notas):

    aprovacao = {'Aprovado': [], 'Reprovado': []}

    for aluno, nota in notas.items():
        if nota >= 7:
            aprovacao['Aprovado'].append(aluno)
        else:
            aprovacao['Reprovado'].append(aluno)

    return aprovacao

print(verificar_aprovacao(notas))