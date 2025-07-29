// F U N Ç Ã O   A N Ô N I M A

let soma = function (a, b) {return a + b; };
console.log(soma(5, 3)); // Saída: 8


// função para definir se um número é par ou ímpar
let parOuImpar = function (num) {
    if(num % 2 == 0){
        return "Par"
    }else{
        return "Ímpar"
    }
}
console.log(parOuImpar(2)) // Saída: Par
console.log(parOuImpar(1)) // Saída: Ímpar


// ARROW FUNCTION = Função seta
let positivoNuloNegativo = (num) => {
    if(num > 0){
        return "Positivo"
    }else if(num == 0){
        return "Nulo"
    }else{
        return "Negativo"
    }
}
console.log(positivoNuloNegativo(2)) // Saída: Positivo
console.log(positivoNuloNegativo(0)) // Saída: Nulo
console.log(positivoNuloNegativo(-1)) // Saída: Negativo


//=========================================================================
// F U N Ç Ã O   C A L L B A C K

function somar(a,b){return a + b}
function subtrair(a,b){return a - b}

function executarOperacao(a,b,operacao){
    return operacao(a,b)
}

console.log(executarOperacao(2, 5, somar)) // Saída: 7
console.log(executarOperacao(5, 2, subtrair)) // Saída: 3

//função callback com função anônima
console.log(executarOperacao(2, 5, (a,b)=>{return a*b})) // Saída: 10


//==========================================================================
// M É T O D O   . m a p ( )

let numeros = [1,2,3,4,5,6,7,8,9,10]

let dobros = numeros.map((num)=>{return num * 2}) 
console.log(dobros) // Saída: [2,4,6,8,10,12,14,16,18,20]


// Exercícios

// Crie um novo array que armazenará o triplo dos números do array numeros
let triplos = numeros.map((num)=>{return num * 3})
console.log(triplos) // Saída: [3,6,9,12,15,18,21,24,27,30]

// Crie um novo array que armazenará o quadrado dos números do array numeros
let quadrados = numeros.map((num)=>{return num ** 2})
console.log(quadrados) // Saída: [1,4,9,16,25,36,49,64,81,100]


//==========================================================================
// M É T O D O   . f i l t e r ( )

let pares = numeros.filter((num)=>{return num % 2 == 0})
console.log(pares) // Saída: [2,4,6,8,10]

// Exercicios

// Façam um novo filtro para armazenar na varíavel impares todos os números ímpares
let impares = numeros.filter((num)=>{return num % 2 == 1})
console.log(impares) // Saída: [1,3,5,7,9]

// Novo array para os próximos exercícios
numeros_novos = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

// Façam um novo array que contenha somente os números positivos
let positivos = numeros_novos.filter((num)=>{return num > 0})
console.log(positivos) // Saída: [1,2,3,4,5]

// Façam um novo array que contenha somente os números negativos
let negativos = numeros_novos.filter((num)=>{return num < 0})
console.log(negativos) // Saída: [-5,-4,-3,-2,-1]



//==========================================================================
// M É T O D O   . r e d u c e ( )

let acumulado = numeros.reduce((acumulador,num)=>{return acumulador + num})
console.log(acumulado) // Saída: 55


// Exercicio

// Ache o maior número entre os dos elementos do novo array
let outros_numeros = [2,14,8,47,5,36,88,1]
let maior = outros_numeros.reduce((acumulador,num)=>{
    if(num > acumulador){
        acumulador = num
    }
    return acumulador
})
console.log(maior) // Saída: 88