# - Crie uma função contar_vogais que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela.

def contar_vogais(palavra: str) -> int:
    """Essa função serve para contar quantas vogais existem numa palavra.
    ----------------------------
    Parâmetros: 
        palavra (str)
    ----------------------------
    Retorna: 
        contador (int)"""
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

palavra = input("Digite uma palavra: ").lower()
print(f"Essa palavra possui {contar_vogais(palavra)} vogais")