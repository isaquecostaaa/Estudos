/**
 * Primitivos (imutáveis) - string, number, boolean, undefined, null
 * 
 * Referência (mutável) - array, object, function
 */

//Primitivos - valores copiados
let a = "a"
let b = a;         // nos tipos primitivos, ao adicionarmos o valor de uma variável a outra é feito apenas uma cópia, 
console.log( a, b);//sendo assim caso a variavel copiada mude de valor a que copiou continua com o valor anterior
console.log( a, b);
a = "Outro valor";
console.log(a, b)

//Referenciais - Passados por referência

let c = [1,2,3];
let d = c;
console.log(c, d) // nos tipos referenciais, as variaveis apontam para um mesmo espaço da memória,
c.push(4)         // então, indepedente de qual variavel seja mudada, todas vão mudar de valor
console.log(c, d)
d.pop()
console.log(c, d)
let e = c;
console.log(e)

let f = [...a] // forma de copiar o valor de a e tornar f independente



const obj = {
    nome:"Isaque"
}

const variavel = obj;
console.log(variavel)
obj.nome = "carlo"
console.log(variavel)