const fizzBuzz = (numero) => {
    if (typeof numero !== 'number') {
        return 'Não é um número'
    }

    if (numero % 5 === 0 && numero % 3 === 0) {
        return 'FizzBuzz';
    } else if (numero % 5 === 0) {
        return 'Buzz';
    } else if (numero % 3 === 0) {
        return 'Fizz';
    } else {
        return numero;
    };

}

console.log(fizzBuzz(Math.floor(Math.random() * (100 - 1) + 1)))