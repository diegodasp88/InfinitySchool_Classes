// Crie uma função que receba um numero inteiro como parâmetro e retorna a sequencia fibonnaci ate aquela ordem respectiva.

function fibonnaci(num){
    let sequencia = []
    for(let i = 0; i < num; i++){
        if(i <= 1){
            sequencia.push(i)
        } else {
            let termo1 = sequencia[i - 2]
            let termo2 = sequencia[i - 1]
            sequencia.push(termo1 + termo2)
        }
    }
    return sequencia
}

let ordem = 8
console.log(fibonnaci(ordem))
for(let i of fibonnaci(ordem)){console.log(i)}