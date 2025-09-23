// Função para abrir o formulário
function abrirFormulario() {
  document.querySelector("#modalCadastroProduto").style.display = "block";
}

// Função para fechar o formulário
function fecharFormulario() {
  document.querySelector("#modalCadastroProduto").style.display = "none";
}

// Fechar o modal se o usuário clicar fora da caixa de conteúdo
window.onclick = function (evento) {
  if (evento.target == document.querySelector("#modalCadastroProduto")) {
    fecharFormulario();
  }
};

const gradeItems = document.querySelector('.grade-itens');

async function carregarProdutos() {
    const url = "https://68d1cee6e6c0cbeb39a5d994.mockapi.io/Produtos";
    const resposta = await fetch(url);
    const data = await resposta.json();
    gradeItems.innerHTML = "";
    data.forEach(produto => {
        gradeItems.innerHTML += `
            <section class="cartao-item" id="produto-${produto.id}">
                <img src="${produto.imagem}" alt="${produto.nome}" />
                <h3>${produto.nome}</h3>
                <p class="preco-item">R$ ${produto.preco}</p>
                <button class="botao-comprar">Comprar</button>
                <button class="botao-excluir" onclick="excluirProduto(${produto.id})">Excluir</button>
            </section>`;
    });
}
carregarProdutos();


async function cadastrarProdutos() {
    const nomeProduto = document.querySelector("#nomeProduto").value;
    const precoProduto = document.querySelector("#precoProduto").value;
    const imagemProduto = document.querySelector("#imagemProduto").value;

    const produto = {
        nome: nomeProduto,
        preco: precoProduto,
        imagem: imagemProduto
    };

    const url = "https://68d1cee6e6c0cbeb39a5d994.mockapi.io/Produtos";

    const resposta = await fetch(url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(produto)
    })
    alert("Produto adicionado com sucesso!")

    fecharFormulario();
    carregarProdutos();
}


async function excluirProduto(id) {
    const url = `https://68d1cee6e6c0cbeb39a5d994.mockapi.io/Produtos/${id}`;
    const resposta = await fetch(url,{ method: "DELETE"});
    if (resposta.status === 200) {
        alert('Produto excluído com sucesso!');
        carregarProdutos();
    } else {
        alert('Erro ao excluir o produto.');
    }
}

