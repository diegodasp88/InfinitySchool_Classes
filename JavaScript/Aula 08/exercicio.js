let carrinho = [
    {
        nome:"Playstation 5",
        preco:3500,
        quantidade:5
    },
    {
        nome:"Bone",
        preco:20,
        quantidade:10
    },
    {
        nome:"Polistation 3",
        preco:250,
        quantidade:4
    },
]

// Filtrar o carrinho somente para produtos com menos de 1000

let filtrar = carrinho.filter((produto)=>{
    return produto.quantidade * produto.preco < 1000
})
console.log(filtrar)

// Reduzir o carrinho em um total de n R$: o resultado tem que dar 18700

let reduzir = carrinho.reduce((acumulador, produto)=>{
    return acumulador += (produto.preco * produto.quantidade)
},0)
console.log(reduzir)