// A R R A Y S

// Índices -->   0          1           2        3
let convidados = ["Gabriel", "Leonardo", "Diego", "Samuel"]

// Imprima no terminal o último elemento
console.log(convidados[(convidados.length)-1])

// Imprima no terminal o primeiro elemento
console.log(convidados[0])

// Imprima no terminal o usuário da posição 1
console.log(convidados[1])

// Faça um sistema que peça o nome do convidado,
// Verifique se esse nome está contido na lista de convidados,
// Se estiver contido, exiba a mensagem: "Seja bem-vindo!",
// Caso contrário, exiba: "Penetra!"

let nome = prompt("Nome do convidado: ")

if(convidados.includes(nome)){
    console.log("Seja bem-vindo")
} else {
    console.log("Penetra!")
}


// (+) Adicionando um elemento no final do array
convidados.push("John")

// (-) Deletando elementos específicos do array usando o índice
    // ([índice incial a ser removido], [quantos elementos a ser removido])
convidados.splice(0, 2) 
    // Deletando somente o elemento de índice 2
convidados.splice(2, 1) // de acordo com a sintaxe, remove 1 elemento a partir do índice 2

// (+) Adicionando elementos num índice específico
convidados.splice(3, 0, "Thais")
    // Nesse caso, a partir do elemento 3, não deletar nenhum elemento (0), e adicionar "Thais" no índice 4

// Encontrando o índice de um elemento do array
convidados.indexOf(nome)
    // Caso o nome digitado não esteja no array, esse método retorna -1

// (-) Deletando o último elemento do array
convidados.pop()

// Fatiamento de array
convidados.slice(2, 5)
    // criar um novo array que inicia no elemento de índice 2 e termina no índice 4