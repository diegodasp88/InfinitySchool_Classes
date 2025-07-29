// function definePar(numero){
//     let resultado

//     if (numero % 2 == 0){
//         resultado = "Par"
//     } else {
//         resultado = "Impar"
//     }

//     return resultado
// }

// console.log( definePar(1) )
// console.log( definePar(2) )
// console.log( definePar(3) )
// console.log( definePar(4) )
// console.log( definePar(5) )
// console.log( definePar(6) )


// function tipoNumero(numero){
//     let tipo
    
//     if(numero > 0){
//         tipo = "Positivo"
//     } else if (numero < 0){
//         tipo = "Negativo"
//     } else {
//         tipo = "Nulo"
//     }

//     return tipo
// }

// console.log( tipoNumero(0) )
// console.log( tipoNumero(1) )
// console.log( tipoNumero(-1) )


function somaNumeros(n1, n2){
    let resultado
    resultado = n1 + n2
    return `${n1} + ${n2} = ${resultado}`
}


function subtraiNumeros(n1, n2){
    let resultado
    resultado = n1 - n2
    return `${n1} - ${n2} = ${resultado}`
}


function multiplicaNumeros(n1, n2){
    let resultado
    resultado = n1 * n2
    return `${n1} * ${n2} = ${resultado}`
}


function divideNumeros(n1, n2){
    let resultado
    resultado = n1 / n2
    return `${n1} / ${n2} = ${resultado}`
}

console.log(somaNumeros(10,5))
console.log(subtraiNumeros(10,5))
console.log(multiplicaNumeros(10,5))
console.log(divideNumeros(10,5))