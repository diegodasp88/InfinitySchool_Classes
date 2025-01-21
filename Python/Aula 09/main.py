import streamlit as st

st.title('Olá mundo!')
st.text('Meu primeiro site com Python!')
st.image('https://imgcdn.stablediffusionweb.com/2024/3/20/874a1a6e-2d08-4c2d-b79f-e8bbe11da55c.jpg')

# texto em Markdown (sintaxe de símbolos para formatação de sites)
st.write('''
# Meu título nível 1

## Meu título nível 2

## Minha lista não ordenada:
- Maçã
- Limão

## Minha Lista ordenada:
1. item 1
2. item 2

## Imagens
![](https://www.artsindia.com/cdn/shop/articles/Lion_Art.jpg?v=1680327542)
''')

# A string de aspas triplas já é interpretado como parte do site, portanto não precisa está contida necessáriamente dentro da função .write()