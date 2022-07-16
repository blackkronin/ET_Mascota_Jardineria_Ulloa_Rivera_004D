function soma() {
    let num1 = parseFloat(document.getElementById("num1").value.replace(",", "."))
    let num2 = parseFloat(document.getElementById("num2").value.replace(",", "."))

    let resultado = document.getElementById("resultado").value = num1 + num2
}

function subtracao() {
    let num1 = parseFloat(document.getElementById("num1").value)
    let num2 = parseFloat(document.getElementById("num2").value)

    let resultado = document.getElementById("resultado").value = num1 - num2
}

function multiplicacao() {
    let num1 = parseFloat(document.getElementById("num1").value)
    let num2 = parseFloat(document.getElementById("num2").value)

    let resultado = document.getElementById("resultado").value = num1 * num2
}

function divisao() {
    let num1 = parseFloat(document.getElementById("num1").value)
    let num2 = parseFloat(document.getElementById("num2").value)

    let resultado = document.getElementById("resultado").value = num1 / num2
}

function imc() {
    let num1 = parseFloat(document.getElementById("num1").value.replace(",", "."))
    let num2 = parseFloat(document.getElementById("num2").value.replace(",", "."))

    let resultado = document.getElementById("resultado").value = (num2 / (num1 * num1)).toFixed(2).replace(".", ",")
    }