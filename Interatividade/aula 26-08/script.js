let inputField = document.getElementById("inputText");
let output = document.getElementById("demo");

inputField.addEventListener('keyup', function(event) {
    output.textContent = "voce pressionou: " + event.key;
    if (event.key === "a" || event.key === "A") {
        alert("letra a digitada");
    }
});

function destacar() {
    document.getElementById("nome").style.backgroundColor = "green";
}

function desfocar() {
    document.getElementById("nome").style.backgroundColor = "white";
}

function colocarMaiuscula(element) {
    element.value = element.value.toUpperCase();
}

function mostraSelecao() {
    let x = document.getElementById("curso").value;
    document.getElementById("botao").innerHTML = "Curso " + x;
}