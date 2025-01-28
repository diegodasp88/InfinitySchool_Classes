import streamlit as st
from tinydb import TinyDB

st.set_page_config(
    page_title='Meus produtos',
    page_icon='🛠️'
)

db = TinyDB('./produtos.json', indent=4)
produtos = db.table('produtos').all()

# Conteúdo do site
with st.sidebar:
    st.title('Cadastro de produtos')

    with st.form('form_produto') as form:
        nome_produto = st.text_input('Nome')
        preco_produto = st.number_input('Preço', step=0.01)
        desc_produto = st.text_area('Descrição')
        
        salvar_produto = st.form_submit_button('Salvar')

    if salvar_produto:
        produto = {
            'Nome': nome_produto,
            'Preço': preco_produto,
            'Descrição': desc_produto
        }
        db.table('produtos').insert(produto)
        produtos = db.table('produtos').all()

st.title('Produtos')
st.table(produtos)