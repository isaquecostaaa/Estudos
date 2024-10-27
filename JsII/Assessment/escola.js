class Livro {
    constructor(titulo, autor, codigo) {
        this.titulo = titulo;
        this.autor = autor;
        this.codigo = codigo;
        this.disponibilidade = true
    }
}

class Leitor {
    constructor(nome, telefone) {
        this.nome = nome;
        this.telefone = telefone;
        this.livros = [];
    }

    adicionarEmprestimo(titulosLivros) {
        this.livros.push(...titulosLivros);
}}

class Emprestimo {
    constructor(leitor, livros) {
        this.leitor = leitor;
        this.data = new Date();
        this.livros = livros;
    }
}

const biblioteca = [];
const leitores = [];
const emprestimos = [];

function adicionarLivro(titulo, autor, codigo) {
    const novoLivro = new Livro(titulo, autor, codigo);
    biblioteca.push(novoLivro);
    console.log("Livro Adicionado com sucesso!")
}

function registrarLeitor(nome, telefone) {
    const novoLeitor = new Leitor(nome, telefone);
    leitores.push(novoLeitor);
    console.log('Leitor registrado.')
}

function criarEmprestimo(leitorAtual, codigos) {
    let livrosEmprestados = [];
    
    const leitor = leitores.find(l => l.nome === leitorAtual);
    if (!leitor) {
        console.log('Leitor não registrado.');
        return;
    }

    codigos.forEach(codigo => {
        let livro = biblioteca.find(livro => livro.codigo === codigo && livro.disponibilidade)
        if (livro) {
            livro.disponibilidade = false;
            livrosEmprestados.push(livro);
        } else {
            console.log('Livro não registrado.');
        }
    });

    if (livrosEmprestados.length > 0) {
        const titulosLivros = livrosEmprestados.map(livro => livro.titulo);  // Pegando apenas os títulos
        const novoEmprestimo = new Emprestimo(leitorAtual, livrosEmprestados);
        
        leitor.adicionarEmprestimo(titulosLivros);
        emprestimos.push(novoEmprestimo)
        console.log('Empréstimo registrado!')
    } else {
        console.log('Os livros selecionados não estão disponíveis.')
    }
    
}

function ExibirEmprestimos(emprestimos) {
    console.log('EMPRÉSTIMOS REGISTRADOS')
    console.log('--------------------------')
    for (let i = 0; i < emprestimos.length; i++) {
        console.log(`Leitor: ${emprestimos[i].leitor}`);
        console.log(`Data: ${registrarData()}`);
        console.log('Livros emprestados:')
        for (let j = 0; j < emprestimos[i].livros.length; j++) {
        console.log(`${j + 1}- ${emprestimos[i].livros[j].titulo}`);
        }
        console.log('--------------------------');
    }
}

function registrarData() {
    const dataAtual = new Date();
    return `${dataAtual.toLocaleString()}`
}

adicionarLivro('naruto', 'mangaka',1234);
adicionarLivro('one piece', "oda genio", 5656)
registrarLeitor('carlao', "2195858844");
registrarLeitor('supimpa',"4022020332")
criarEmprestimo('carlao',[1234])
criarEmprestimo('supimpa',[1234, 5656])



  
ExibirEmprestimos(emprestimos)

