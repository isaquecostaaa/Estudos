class Livro {
    constructor(codigo, titulo, taxa) {
        this.codigo = codigo;
        this.titulo = titulo;
        this.taxa = taxa;
        this.disponibilidade = true
    }
}

class Leitor {
    constructor(nome, telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }
}

class Emprestimo {
    constructor(leitor, identificacao) {
        this.leitor = leitor;
        this.identificacao = identificacao;
        this.livros = [];
    }

    registrar() {
        emprestimos.push(this)
    }

    addLivro(livro) {
        this.livros.push(livro)
    }

    removerLivro(codigo) {
        const index = this.livros.findIndex(livro => livro.codigo == codigo)
        if (index !== -1) {
            this.livros.splice(index, 1);
        } else {
            alert(`Livro com código ${codigo} não encontrado!`);
        }
    }

    alterarAtributo(atributo, novoValor) {
        if(this[atributo] !== undefined) {
            this[atributo] = novoValor
        } else {
            console.log('Atributo não encontrado')
        }
    }
}