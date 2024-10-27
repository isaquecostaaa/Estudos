function contarPares() {

    for (let num = 1; num <= 20; num++) {

        if (num % 2 == 0) {
            console.log(num)
        }
    }
}
contarPares()

/**
 * Objetivo: Implementar um loop for para contar e exibir os números pares de 1 a 20.

Requisitos:

Crie uma função chamada contarPares que não recebe nenhum parâmetro.
Dentro da função, utilize um loop for para iterar de 1 até 20.
Verifique se o número atual é par (divisível por 2).
Se for par, exiba o número.
Dica: Utilize o operador de módulo % para verificar se um número é par.
 */

function somarImpares() {
    let somar = 0;
    for (let num = 1; num <= 15; num++) {
        
        if (num % 2 !== 0) {
            somar += num;
        }
    }
    console.log(somar)
    
}

somarImpares()

/**
 * Objetivo: Calcular a soma dos números ímpares de 1 a 15 utilizando um loop for.

Requisitos:

Crie uma função chamada somarImpares que não recebe nenhum parâmetro.
Dentro da função, utilize um loop for para iterar de 1 até 15.
Verifique se o número atual é ímpar.
Se for ímpar, adicione-o a uma variável acumuladora.
No final do loop, exiba a soma dos números ímpares.
 */

function multiplicarArray(numeros) {
    let multiplicador = [];
    for (let i = 0; i < numeros.length; i++) {
        
        multiplicador.push(numeros[i] * 3)
    }
    return multiplicador
}
 const numeros = [1,2,3,4,5,6]
 const novoArray = multiplicarArray(numeros)
 console.log(novoArray)

 /**
 * Objetivo: Multiplicar cada elemento de um array por 3 e armazenar os resultados em um novo array.

Requisitos:

Crie uma função chamada multiplicarArray que recebe um array de números como parâmetro.
Dentro da função, inicialize um novo array vazio para armazenar os resultados.
Utilize um loop for para iterar sobre cada elemento do array passado como parâmetro.
Multiplique cada elemento por 3 e adicione o resultado ao novo array.
Retorne o novo array contendo os resultados.
Dica: Utilize o método push para adicionar elementos ao novo array.
 */

function exibirCarro() {
    const carro = {
        marca: "Toyota",
        modelo: "Corolla",
        ano: 2020
    }

    for (let prop in carro) {
        console.log(prop + ": " + carro[prop])
    }
}
exibirCarro()

/**
 * Objetivo: Implementar um loop for..in para percorrer e exibir as propriedades e valores de um objeto que representa um carro.

Requisitos:

Crie uma função chamada exibirCarro que não recebe nenhum parâmetro.
Dentro da função, crie um objeto chamado carro com as seguintes propriedades:
marca: "Toyota"
modelo: "Corolla"
ano: 2020
Utilize um loop for..in para iterar sobre as propriedades do objeto carro.
Durante a iteração, exiba cada propriedade e seu respectivo valor no formato: propriedade: valor.
 */


function contarPropriedades(pessoa) {
    let contador = 0;
    for (let prop in pessoa) {
        contador++
    }
    console.log(contador)
};

const pessoa = {
    nome: "Ana",
    idade: 28,
    profissao: "Engenheira"
};

contarPropriedades(pessoa);

/**
 * Objetivo: Contar quantas propriedades um objeto possui utilizando um loop for..in.

Requisitos:

Crie uma função chamada contarPropriedades que recebe um objeto como parâmetro.
Inicialize uma variável acumuladora para contar as propriedades.
Utilize um loop for..in para iterar sobre as propriedades do objeto.
Para cada propriedade, incremente a variável acumuladora.
No final do loop, exiba o número total de propriedades do objeto.
 */

function exibirElementosArrayNum(arrayNumeros) {
    for (let indice in arrayNumeros) {
        console.log(`Índice ${indice}: ${arrayNumeros[indice]}`)
    }
};

const arrayNumeros = [10, 20, 30, 40, 50];
exibirElementosArrayNum(arrayNumeros);

/**
 * Objetivo: Utilizar for..in para iterar sobre os índices de um array e exibir os elementos.

Requisitos:

Crie uma função chamada exibirElementosArray que recebe um array de números como parâmetro.
Dentro da função, utilize um loop for..in para iterar sobre os índices do array.
Durante a iteração, exiba o índice atual e o elemento correspondente do array no formato: Índice X: valor.
 */

function exibirElementosArray() {
    const frutas = ["Maçã", "Banana", "Laranja", "Manga"]

    for (let fruta of frutas) {
        console.log(fruta)
    }
}

exibirElementosArray()

/**
 * Objetivo: Implementar um loop for..of para iterar sobre os elementos de um array e exibi-los.

Requisitos:

Crie uma função chamada exibirElementosArray que não recebe nenhum parâmetro.
Dentro da função, crie um array chamado frutas com os seguintes elementos: "Maçã", "Banana", "Laranja", "Manga".
Utilize um loop for..of para iterar sobre os elementos do array frutas.
Durante a iteração, exiba cada elemento do array.
 */

function contarCaracteres(texto) {
    let totalCaracteres = 0;
    for (let caracteres of texto) {
        totalCaracteres++
    }
    console.log(`Total: ${totalCaracteres} caracteres`)
}
const mensagem = "Olá, mundo!";
contarCaracteres(mensagem); 

/**
 * Objetivo: Utilizar for..of para contar o número total de caracteres em uma string.

Requisitos:

Crie uma função chamada contarCaracteres que recebe uma string como parâmetro.
Inicialize uma variável acumuladora para contar os caracteres.
Utilize um loop for..of para iterar sobre cada caractere da string.
Para cada caractere, incremente a variável acumuladora.
No final do loop, exiba o número total de caracteres da string.
 */

