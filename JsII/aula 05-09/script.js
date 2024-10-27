const valores = [1,2,3,4,5,6];

const dobro = valores.map((valor) => valor * 2);
console.log(dobro);

const produtos = [
    {nome: "Camisa", preco: 100},
    {nome: "Tenis", preco: 150},
    {nome: "Bermuda", preco: 200}
];

function aplicarDesconto(colecao) {
    return colecao.map((p) => {
        return {
            nome: p.nome,
            preco: p.preco - (p.preco * 0.1)
        }
    })
}

const desconto = aplicarDesconto(produtos)
console.log(desconto)


const alunos = ["Mayara Araujo", "Arthur Barcellos", "Vinicius Holanda"];

const iniciais = alunos.map((aluno) => 
    aluno.split(" ").map((palavra) => palavra.charAt(0).toUpperCase()).join("")
);
console.log(iniciais);