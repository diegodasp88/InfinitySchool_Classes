// Crie uma função chamada fatorial que calcule o fatorial de um número.

function fatorial(num){
    let fatorial = 1
    for(let i = 1; i <= num; i++){
        fatorial *= i
    }
    return fatorial
}

console.log(fatorial(4))