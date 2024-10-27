const locacoes = [];

class Filme {
    constructor(titulo, codigo) {
        this.titulo = titulo;
        this.codigo = codigo;
        this.disponivel = true;
    }
}

class Cliente {
    constructor(nome, email) {
        this.nome = nome;
        this.email = email;
    }
}

class Locacao {
    constructor(codigo, cliente) {
        this.codigo = codigo;
        this.cliente = cliente;
        this.filmes = [];
    }

    adicionarFilme(filme) {
        this.filmes.push(filme)
    }

    registrarLocacao() {
        locacoes.push(this);
    }
}

function adicionarLocacao() {
    const nome = prompt('Digite o nome do cliente:');
    const email = prompt('Digite o email do cliente:');
    const codigo = prompt('Digite o codigo da locação');

    const novoCliente = new Cliente(nome, email);
    const novaLocacao = new Locacao(novoCliente, codigo);

    novaLocacao.registrarLocacao();
}

function 