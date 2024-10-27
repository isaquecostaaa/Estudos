const num = parseFloat(prompt("digite um número:"));
let element = document.getElementById("numero");
let box = document.getElementById("box");


element.innerHTML = num;
box.innerHTML += `<p>Raiz quadrada: ${num ** 0.5}</p>`;
box.innerHTML += `<p>É inteiro: ${Number.isInteger(num)}</p>`;
box.innerHTML += `<p>É NaN: ${Number.isNaN(num)}</p>`;
box.innerHTML += `<p>Arredondado pra baixo: ${Math.floor(num)}</p>`;
box.innerHTML += `<p>Arredondado pra cima: ${Math.ceil(num)}</p>`;
box.innerHTML += `<p>Com duas casas decimais: ${num.toFixed(2)}</p>`;

// "=" muda o valor do inner pra um novo e "+=" adiciona um valor novo