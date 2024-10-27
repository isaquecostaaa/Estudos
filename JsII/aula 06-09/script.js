const valores = [1,2,3,4,5];

const dobro = valores.map((valor) => valor * 2)
console.log(dobro);


const frutas = ['maça', 'banana', 'uva'];

const maiusculo = frutas.map((fruta) => fruta.toUpperCase());
console.log(maiusculo);

const pessoas = [
    {
        nome: "João",
        idade: 25 } ,
    {
        nome: "Maria",
        idade: 30
    }]

const nomes = pessoas.map((pessoa) => pessoa.nome);
console.log(nomes)

const precos = [100, 200, 300];

const precoImposto = precos.map((preco) => preco + (preco * 0.10));
console.log(precoImposto)

const celsius = [0,20,30];

const f = celsius.map((c) => (c * 9/5) + 32);
console.log(f)

const datas = ["2024-09-06", "2023-05-12"]

const datasFormatas = datas.map((data) => {
    data.slice("-")
}) 