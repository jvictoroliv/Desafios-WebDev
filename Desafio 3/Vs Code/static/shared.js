// shared.js

// Função para decrementar a quantidade
function decrement() {
    var qtyInput = document.getElementById("qtyInput");
    var qty = parseInt(qtyInput.value);
    if (qty > 1) {
        qtyInput.value = qty - 1;
    }
}

// Função para incrementar a quantidade
function increment() {
    var qtyInput = document.getElementById("qtyInput");
    var qty = parseInt(qtyInput.value);
    qtyInput.value = qty + 1;
}

// Suponhamos que você tenha um elemento de quantidade e um elemento de preço no seu HTML
var quantidadeElement = document.getElementById("qtyInput");
var precoElement = document.getElementById("precoProduto");

// Selecione o elemento onde você deseja exibir o resultado
var resultadoElement = document.getElementById("resultado");

// Função para calcular o resultado
function calcularResultado() {
    var quantidade = parseInt(quantidadeElement.value);
    var preco = parseFloat(precoElement.textContent.replace("R$ ", ""));
    var resultado = quantidade * preco;

    // Atualize o texto no elemento de resultado
    resultadoElement.textContent = "Total: R$ " + resultado.toFixed(2);
}

// Adicione ouvintes de evento para detectar mudanças na quantidade e no preço
quantidadeElement.addEventListener("input", calcularResultado);
precoElement.addEventListener("input", calcularResultado);

// Chame a função inicialmente para exibir o resultado
calcularResultado();

