let numeros = [1,2,3,4,5,6,7,8,9,10,11]

let dobros = numeros.map((n)=>{return n * 2})
console.log(`Lista de dobros: [${dobros}]`)

let pares = numeros.filter((n)=>{return n % 2 == 0})
console.log(`Lista de números pares: [${pares}]`)

let somaTotal = numeros.reduce((acumulador,n)=>{return acumulador + n},0)
console.log(`Soma de todos os elementos: ${somaTotal}`)

// façam o filtro de impares baseado no array numeros original
let impares = numeros.filter((n)=>{return n % 2 == 1})
console.log(`Lista de números ímpares: [${impares}]`)
        
// Façam o quintuplo dos valores do array de numeros 
let quintuplo = numeros.map((n)=>{return n * 5})
console.log(`Lista de quíntuplos: [${quintuplo}]`)
        
// Faça o filtro do array original para armazenar somente os primos ---> somente tem 2 divisores
let primos = numeros.filter((n)=>{
    let divisores = 0
    for(let i = n; i > 0; i--){
        if(n % i == 0){
            divisores += 1
        }
    }
    if(divisores == 2){
        return n
    }
})
console.log(`Lista de números primos: [${primos}]`)