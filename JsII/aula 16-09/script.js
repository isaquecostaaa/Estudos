const valoresA = [10, 15, 20, 25, 30]
const valoresB = [1, 5, 2, 7, 8]
const valoresC = [100, 150, 200, 250, 300]

const filtrarValoresPares = (osValores) => osValores.filter(valor => valor % 2 === 0)

console.log(filtrarValoresPares(valoresA))
console.log(filtrarValoresPares(valoresB))
console.log(filtrarValoresPares(valoresC))

//------------------------------------

const programadores = [
    {nome: 'Arthur', idade: 30},
    {nome: 'Danillo', idade: 50},
    {nome: 'Larissa', idade: 20},
    {nome: 'Matheus', idade: 40},
];



const filtrarProgramadoresVelhos = (devs) => devs.filter((dev) => dev.idade > 25);

console.log(filtrarProgramadoresVelhos(programadores))

//---------------------------------------------

const disciplinas = [
    'JavaScript básico',
    'O intermediário do JavaScript',
    'Python para doidos',
    'Java para Mateus',
    'Outras disciplinas',
];

const filtrarLinguagem = (disciplinas, linguagem) => disciplinas.filter(disciplina => disciplina.includes(linguagem))

console.log(filtrarLinguagem(disciplinas, "JavaScript"))
console.log(filtrarLinguagem(disciplinas, "Python"))

//---------------------------------------------

const posicoes = ['goleiro', 'lateral', 'zagueiro', 'atacante'];

const existePosicao = (posicoes, posicao) => posicoes.includes(posicao);

console.log(existePosicao(posicoes, "goleiro"));
console.log(existePosicao(posicoes, "lateral"));
console.log(existePosicao(posicoes, "meia"));

//---------------------------------------------

const filtrarPorLetra = (posicoes, letra) => posicoes.filter(posicao => posicao.includes(letra))

console.log(filtrarPorLetra(posicoes, "t"))
console.log(filtrarPorLetra(posicoes, "e"))
console.log(filtrarPorLetra(posicoes, "g"))

//---------------------------------------------

const verificarExistencia = (textos, palavra) => textos.some(texto => texto.includes(palavra))

console.log(verificarExistencia(disciplinas, "doidos"))
