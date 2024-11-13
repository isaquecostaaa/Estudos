# Entre com uma lista de nomes alunos e notas (n1 e n2) terminada com nome igual a "fim"
# Mostrar as médias dos alunos
# Alunos aprovados e em prova final (média >= 6 para aprovação

MEDIA_APROVACAO = 6.0
FLAG = "fim"
MIN_TAM_NOME = 4

def entrar_nome():
    while (True):
        nome = input('Entre com o nome: ')
        if (len(nome) < MIN_TAM_NOME):
            print("Erro: nome inválido")
        else:
            break
    return nome

def entrar_nota(msg):
    while (True):
        try:
            nota = float(input(msg))
            break
        except:
            print("Nota invállida")
        return nota


def entrar_alunos():
    turma = []
    nome = input("Entre com o nome: ")
    while(nome.lower() != FLAG):
        nota1 = entrar_nota("Entre com a primeira nota: ")
        nota2 = entrar_nota("Entre com a segunda nota: ")
        aluno = [nome, nota1, nota2]
        turma.append(aluno)
        nome = input("Entre com o nome: ")
    return turma

def exibir_turma(turma):
    for aluno in turma:
        print(aluno)

def calcular_medias(turma):
    medias = []
    for aluno in turma:
        soma = aluno[1] + aluno[2]
        media = soma / 2
        medias.append([aluno[0], media])
    return medias

def exibir_medias(medias):
    for media in medias:
        print(media)

def exibir_aprovacao(medias):
    for aluno in medias:
        if (aluno[1] >= MEDIA_APROVACAO):
            print(aluno[0], "aprovado")
        else:
            print(aluno[0], "prova final")

turma = entrar_alunos()  #[["André",8,9],["Bruno",5,8],["Carlos",8,9],["Eloisa",9,6]]
exibir_turma(turma)



