//break - interrompe a iteração
// continue - para a iteração atual e pula pra próxima
const numeros = [1,2,3,4,5,6,7,8];

for (let numero of numeros) {

    if (numero === 2) {
        console.log('pulei')
        continue;
    }

    if (numero === 7) {
        console.log('achei');
        break;
    }


    console.log(numero);
}