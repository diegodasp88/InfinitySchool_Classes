// O B J E T O S 

let clienteObjeto = {
    nome: "Diego",
    idade: 36
}

// Adicionado chaves e valores ao objeto:
clienteObjeto.profissao = "Aux. Contabilidade"
clienteObjeto.saldoConta = 100000
clienteObjeto.numeroConta = "12345-6"

//=========================================================
// Criando funções anônimas dentro do objeto
let cliente = {
    nome: "Diego",
    idade: 36,
    saldo: 100000,
    numeroConta: "12345-6",
    depositar: function(valor){
        this.saldo += valor
    },
    sacar: function(valor){
        this.saldo -= valor
    }
}

console.log(cliente.saldo)
cliente.depositar(1000)
console.log(cliente.saldo)
cliente.sacar(500)
console.log(cliente.saldo)

//=========================================================
// Transformando um Object em JSON

let clienteJSON = JSON.stringify(cliente)
console.log(clienteJSON)
console.log(typeof(clienteJSON))


//=========================================================
// Criando arrays de chaves (keys)
let chaves = Object.keys(cliente)

// Para iterar um objeto é necessário criar um array das chaves
for (chave of chaves){
    console.log(`${chave} - ${cliente[chave]}`)
}

// Criando arrays de valores (values)
let valores = Object.values(cliente)

// Iterando um objeto usando os arrays de chaves e valores
for (let i = 0; i < chaves.length; i++){
    console.log(`${chaves[i]} - ${valores[i]}`)
}


//=========================================================
// Destructuring Objects - Desconstruindo objetos

// basta declarar as chaves do objeto dentre chaves recebendo o nome do objeto
// assim são criadas novas variáveis com o nome das chaves que podem ser acessadas
let {nome, idade} = cliente
console.log(nome)
console.log(idade)