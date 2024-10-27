const numeros = [1000,2000,3000,4000,5000,6000,7000,8000,9000];
const [um, , tres, , cinco, , sete] = numeros;
console.log(um, tres, cinco);

const numbers = [[1,2,3],[4,5,6],[7,8,9]];
const [,[,,sesus]] = numbers;
console.log(sesus);

const pessoa = {nome: 'isaque', sobrenome: 'costa', endereco: 'josevalente'};

const {nome, sobrenome} = pessoa;
console.log(nome, sobrenome)

const {endereco : {rua, numero}} = pessoa;
console.lof