let codigoEmprestimo = 0;
let indexLivro = 0;

const leitores = [
    "Steve Jobs",
  "Bill Gates",
  "Elon Musk",
  "Mark Zuckerberg",
  "Tim Berners-Lee",
  "Ada Lovelace",
  "Linus Torvalds",
  "Jeff Bezos",
  "Sheryl Sandberg",
  "Sundar Pichai",
]

function gerarNumeroTelefone() {
    const ddd = String(Math.floor(Math.random() * 90) + 10);
    const numero = String(Math.floor(Math.random() * 90000000) + 30000000);
    return `(${ddd}) ${numero}`;
}

const emprestimos = [];
const biblioteca = [
    { codigo: 1, titulo: "1984", taxa: 10.99, disponibilidade: true},
    { codigo: 2, titulo: "Dom Casmurro", taxa: 10.99, disponibilidade: true},
    { codigo: 3, titulo: "O Senhor dos Anéis: A Sociedade do Anel", taxa: 10.99, disponibilidade: true },
    { codigo: 4, titulo: "O Alquimista", taxa: 10.99, disponibilidade: true },
    { codigo: 5, titulo: "A Revolução dos Bichos", taxa: 10.99, disponibilidade: true },
    { codigo: 6, titulo: "Orgulho e Preconceito", taxa: 10.99, disponibilidade: true},
    { codigo: 7, titulo: "Harry Potter e a Pedra Filosofal", taxa: 10.99, disponibilidade: true},
    { codigo: 8, titulo: "O Pequeno Príncipe", taxa: 10.99, disponibilidade: true},
    { codigo: 9, titulo: "A Menina que Roubava Livros", taxa: 10.99, disponibilidade: true},
    { codigo: 10, titulo: "Cem Anos de Solidão", taxa: 10.99, disponibilidade: true}
];

class Livro {
    constructor(titulo, taxa) {
        this.codigo = biblioteca.length + 1;
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
        this.status = 'Em aberto'
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

    alterarAtributo(novoStatus) {
        this.status = novoStatus;
    }
}

function menuEmprestimoOuLivro() {
    const escolha = prompt("Digite 1 para registrar um novo empréstimo\n Digite 2 para adicionar um novo livro à biblioteca");

    if (escolha === '1') {
        coletarDadosEmprestimo();
    } else if (escolha === '2') {
        criarLivro();
    } else {
        alert("Opção inválida. Por favor, escolha 1 ou 2.");
        menuEmprestimoOuLivro();
    }
}

function criarLivro() {
    const titulo = prompt("Digite o título do livro:");
    const taxa = parseFloat(prompt("Digite a taxa de empréstimo do livro:"));

    const novoLivro = new Livro(titulo, taxa);
    
    biblioteca.push(novoLivro);
    
    alert(`Livro '${novoLivro.titulo}' adicionado à biblioteca com sucesso!`);
    menuEmprestimoOuLivro();
}

function exibirEmprestimos() {
    let mensagem = "empréstimos: \n";

    emprestimos.forEach((emprestimo, i) => {
        mensagem += `${++i}- Empréstimo\nLeitor: ${emprestimo.leitor.nome} \n ID: ${emprestimo.identificacao}\n Status: ${emprestimo.status}\n`;
        mensagem += `Livros: \n`
        emprestimo.livros.forEach((livro, j) => {
            mensagem += `   ${++j}- ${livro.titulo} - Código: ${livro.codigo}\n`
         })
         mensagem += '------------------------------\n'
    })
    alert(mensagem)
}

function coletarDadosEmprestimo() {
    
    
    const nomeLeitor = prompt("Digite o nome do leitor:", leitores[codigoEmprestimo]);
    const telefoneLeitor = prompt("Digite o telefone do leitor:", gerarNumeroTelefone())
    const identificacao = parseInt(prompt("Digite o ID do empréstimo:", ++codigoEmprestimo));

    const leitor = new Leitor(nomeLeitor, telefoneLeitor)
    const emprestimo = new Emprestimo(leitor, identificacao)


    coletarLivroDisponivel(emprestimo);

    emprestimo.registrar()

    if(confirm('deseja continuar?')) {
        coletarDadosEmprestimo()
    } 
}

function coletarLivroDisponivel(emprestimo) {

    let mensagem = "Livros disponíveis para empréstimo:\n";
    const livrosDisponiveis = biblioteca.filter(livro => livro.disponibilidade);

    if (livrosDisponiveis.length === 0) {
        alert("Nenhum livro disponível para empréstimo.");
        return;
    }

    livrosDisponiveis.forEach((livro, index) => {
        mensagem += `${index + 1} - Código: ${livro.codigo}, Título: ${livro.titulo}, Taxa: ${livro.taxa}\n`;
    });

    alert(mensagem);

    const codigoLivro = parseInt(prompt("Digite o código do livro que deseja adicionar ao empréstimo:", biblioteca[indexLivro].codigo));
    indexLivro++
    const livroSelecionado = livrosDisponiveis.find(livro => livro.codigo === codigoLivro);

    if (livroSelecionado) {
        livroSelecionado.disponibilidade = false;
        emprestimo.addLivro(livroSelecionado); // Adiciona o livro ao empréstimo
        alert(`Livro '${livroSelecionado.titulo}' adicionado ao empréstimo.`);
    } else {
        alert("Livro não encontrado ou indisponível.");
    }

    if (confirm("Deseja adicionar outro livro?")) {
        coletarLivroDisponivel(emprestimo);
    }
}

function excluirLivro() {
    const codigoEmprestimo = parseInt(prompt('Digite o ID do empréstimo do qual deseja remover umm livro:'))
    const emprestimoEncontrado = emprestimos.find(emprestimo => emprestimo.identificacao === codigoEmprestimo);

     

    if (emprestimoEncontrado) {
        let txt = `Empréstimo selecionado: \n ID: ${emprestimoEncontrado.identificacao}\n`;
        emprestimoEncontrado.livros.forEach((livro, index) => {
            txt += `${++index}- ${livro.titulo} - Código: ${livro.codigo}\n`;
        });
        alert(txt);

        const codigoLivro = parseInt(prompt('Digite o código do Livro que deseja remover:'));
        emprestimoEncontrado.removerLivro(codigoLivro);
        alert(`Livro com código ${codigoLivro} removido com sucesso.`)
        let txtAtualizado = `Empréstimo atualizado: \n ID: ${emprestimoEncontrado.identificacao}\n`;
        emprestimoEncontrado.livros.forEach((livro, index) => {
            txtAtualizado += `${++index}- ${livro.titulo} - Código: ${livro.codigo}\n`;
        });
        alert(txtAtualizado);
    } else {
        console.log('Empréstimo não encontrado.')
    }
    
}

function alterarStatusEmprestimo() {
    const codigoEmprestimo = parseInt(prompt('Digite o ID do empréstimo do qual deseja alterar o status:'))
    const emprestimoEncontrado = emprestimos.find(emprestimo => emprestimo.identificacao === codigoEmprestimo);

    txt = 'Digite o número correspondente a opção desejada\n 1 - Em aberto\n2 - Atrasado\n3 - Pago'

    const novoStatus = prompt(txt);

    switch (novoStatus) {
        case '1':
            emprestimoEncontrado.alterarAtributo('Em aberto');
            alert('Status atualizado com sucesso.')
        break;
        case '2':
            emprestimoEncontrado.alterarAtributo('Atrasado');
            alert('Status atualizado com sucesso.')
        break;
        case '3':
            emprestimoEncontrado.alterarAtributo('Pago');
            alert('Status atualizado com sucesso.')
        break;
        default:
            alert('Opção não válida.');
            return alterarStatusEmprestimo();
    }
}

const calcularTotalizadoresEmprestimos = (emprestimos) => 
    emprestimos.map(emprestimo => {
        const totalLivros = emprestimo.livros.length;
        const valorTotal = emprestimo.livros.reduce((total, livro) => total + parseFloat(livro.taxa), 0);

        return {
            idEmprestimo: emprestimo.identificacao,
            leitor: emprestimo.leitor.nome,
            totalLivros: totalLivros,
            valorTotal: valorTotal,
        };
    });

function exibirTotalizadores() {
    const totalizadoresEmprestimos = calcularTotalizadoresEmprestimos(emprestimos)

    let txt = "EMPRÉSTIMOS TOTALIZADOS:\n";
    totalizadoresEmprestimos.forEach(total => {
        txt += `ID: ${total.idEmprestimo} \nLeitor: ${total.leitor} \nTotal de livros: ${total.totalLivros} \nValor Total: ${Math.floor(total.valorTotal).toFixed(2)}\n`
        txt += '----------------------------\n'
    })
    console.log(txt)
}

const encontrarEmprestimosMultiplos = (emprestimos) => 
    emprestimos.filter(emprestimo => emprestimo.livros.length > 1);

function exibirMultiplos() {
    const emprestimosMultiplos = encontrarEmprestimosMultiplos(emprestimos);
    if (emprestimosMultiplos.length > 0) {
        let txt = "EMPRÉSTIMOS COM MAIS DE UM LIVRO:\n";
        emprestimosMultiplos.forEach((emprestimo, i) => {
          txt += `${++i} - ID: ${emprestimo.identificacao} \nLeitor: ${
            emprestimo.leitor.nome
          } \nLivros:\n`;
          emprestimo.livros.forEach((livro, j) => {
            txt += `    ${++j} - ${livro.titulo}\n`;
          });
          txt += "------------------------------\n";
        });
        console.log(txt);
        } else {
          console.log('Não existem empréstimos com mais de um livro.')
        }
}

const existeEmprestimoComCincoLivros = (emprestimos) => {

    const emprestimoCincoLivros = emprestimos.some(emprestimo => emprestimo.livros.length >= 5)
        console.log(emprestimoCincoLivros ? `Existem empréstimos com 5 ou mais livros (${emprestimoCincoLivros})` :`Não existem empréstimos com 5 ou mais livros (${emprestimoCincoLivros})`)
}

function gerarRelatorioDetalhado() {
    if (emprestimos.length === 0) {
        alert("Não há empréstimos registrados.");
        return;
    }

    let relatorio = "RELATÓRIO DE EMPRÉSTIMOS\n";
    relatorio += "=========================\n";

    emprestimos.forEach((emprestimo, index) => {
        const nomeLeitor = emprestimo.leitor.nome.toUpperCase();
        const telefoneLeitor = emprestimo.leitor.telefone.replace(/[^0-9]/g, '');

        relatorio += `EMPRÉSTIMO #${index + 1}\n`;
        relatorio += `Leitor: ${nomeLeitor}\n`;
        relatorio += `Telefone: ${telefoneLeitor}\n`;
        relatorio += `ID do Empréstimo: ${emprestimo.identificacao}\n`;
        relatorio += `Status: ${emprestimo.status}\n`;
        relatorio += `Livros Emprestados:\n`;
        emprestimo.livros.forEach(livro => {
            const tituloFormatado = livro.titulo.substring(0, 1).toUpperCase() + livro.titulo.substring(1).toLowerCase();
            const taxaArredondada = Math.round(livro.taxa);
            relatorio += `- ${tituloFormatado} (Código: ${livro.codigo}, Preço: R$ ${taxaArredondada})\n`;
        });

        relatorio += "-------------------------\n";
    });

    alert(relatorio);
}


menuEmprestimoOuLivro()
exibirEmprestimos()
excluirLivro()
alterarStatusEmprestimo()
exibirTotalizadores()
exibirMultiplos()
existeEmprestimoComCincoLivros(emprestimos)
gerarRelatorioDetalhado()