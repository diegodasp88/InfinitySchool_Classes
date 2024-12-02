# Ex 03. Dado o dicionário abaixo, remova o item com a 
# chave "banana" (utilizando a função pop()) e exiba o dicionário atualizado.
'''python
    estoque = {"banana": 10, "laranja": 5, "uva": 8}
'''

estoque = {"banana": 10, "laranja": 5, "uva": 8}
print(f'Estoque inicial: {estoque}\n')
estoque.pop('banana')
print(f'Estoque atual: {estoque}\n')
