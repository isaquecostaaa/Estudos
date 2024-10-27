/* const data = new Date("2019-04-20 20:15:59.100" );
console.log(data.toString())
console.log(data.getDate())
console.log(data.getMonth())
console.log(data.getFullYear())
console.log(data.getHours())
console.log(data.getMinutes())
console.log(data.getSeconds())
console.log(data.getMilliseconds())
console.log(data.getDay());
console.log(Date.now()) */

function zero(num) {
    return num > 10 ? num : `0${num}`;
}

function datas(data) {
    const dia = zero(data.getDate());
    const mes = zero(data.getMonth());
    const ano = zero(data.getFullYear());
    const hora = zero(data.getHours());
    const min = zero(data.getMinutes());
    const seg = zero(data.getSeconds());

    return `${dia}/${mes}/${ano} ${hora}:${min}:${seg}`
}

const data = new Date();
const datasbrasil = datas(data)
console.log(datasbrasil)