function saudacao(nome) {

    return "olá " + nome 
}
let nome = "carlao"
saudacao(nome)
saudacao("maria")
const valor = saudacao("matildo")
console.log(valor)

function soma(x = 10, y = 10) {
    const resultado = x + y
return resultado; // assim que o programa encontrar a palavra return a funcao encerra
}

console.log(soma(2, 2))
console.log(soma(3, 5))
console.log(soma(8, 2))
console.log(soma()) // sempre que os parametros nao sao informados o padrão é executado, caso possua

const resultado = soma(2, 2)
console.log(resultado)

// função em variavel
const raiz = function(n) {
return n ** 0.5;
};

console.log(raiz(9))

//função em arrow function

const raizes = n => n ** 0.5;
console.log(raizes(25))
