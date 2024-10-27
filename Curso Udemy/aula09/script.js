// for in: lê os indices de um array ou o nome das propriedades de um objeto
// for of: lê os valores de um array ou dos item de um objeto

const frutas = ['pera', 'maça', 'uva'];

for (let indice in frutas) {
    console.log(indice); // lê o indice do array 
}
for (let indice in frutas) {
    console.log(frutas[indice]); // lê o valor referente ao indice do array
}

for (let fruta of frutas) {
    console.log(fruta); // lê o valor do item do array na ordem
}

const pessoa = {
    nome: 'isaque',
    sobrenome: 'costa',
    idade: 20
}

for (let prop in pessoa) {
    console.log(prop); // lê o o nome das propriedades do objeto
}

const nome = 'isaque costa';

for (let i in nome) {
    console.log(nome[i]);
}

for (let i of nome) {
    console.log(i)
}