const pessoa = {
    nome: "Isaque",
    sobrenome: "Costa",
    idade: 25
};

console.log(pessoa.nome)

function criarPessoa(nome, sobrenome, idade) {
    return {
        nome: nome,
        sobrenome: sobrenome,
        idade: idade
    }
}

const pessoa2 = criarPessoa("carlito", "junio", 43)
const pessoa3 = criarPessoa("wesley", "junio", 43)
const pessoa4 = criarPessoa("nivaldo", "junio", 43)
console.log(pessoa2.nome, pessoa3.nome, pessoa4.nome)

const pessoa5 = {
    nome: "arlindo",

    fala() { // funções dentro de objetos se chamam metodos
        console.log(this.nome) // this se refere ao objeto
    }
}

pessoa5.fala();