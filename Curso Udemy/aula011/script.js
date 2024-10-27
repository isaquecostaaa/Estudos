function maiorNumero(num1, num2) {
    if (num1 > num2) {
        return `O maior numero é ${num1}`;
    } else if (num1 === num2) {
        return 'Os números são iguais'
    };
    return `O maior numero é ${num1}`;
};

console.log(maiorNumero(2,2));