
//                 0      1       2   
const alunos = ['Luiz','Maria','João']
console.log(alunos)
console.log(alunos[0])
console.log(alunos[2])

console.log( alunos instanceof Array) // verifica se a variavel é um array

alunos[alunos.length] = "carlao" // adiciona ao final de acordo com o tamanho do array

alunos.push("isaque") // adiciona ao final do array

alunos.unshift("joaozinho") // adiciona no começo e empurra outros elementos pro lado
console.log(alunos)
removido1 = alunos.shift(); // remove o primeiro elemento ajustando os indices do array
console.log(removido1)
removido2 = alunos.pop(); // remove o ultimo elemento do array ajustando os indices do array
console.log(removido2);

delete alunos[2]; // remove um elemento sem alterar os indices (o elemento removido fica como vazio)
console.log(alunos);

console.log(alunos.slice(0, 3)) // fatiando array pra selecionar elementos especificos ( do 0 até 2, o 3 não é incluido)
console.log(alunos.slice(0, -3)) // usando numeros negativos a função vai eliminar de trás pra frente