import streamlit as st

st.title('Soma de números')

with st.form('soma_numeros') as form:
    n1 = st.number_input('1º número', step=1)
    n2 = st.number_input('2º número', step=1)
    somar = st.form_submit_button('Sum')
    subtrair = st.form_submit_button('Sub')
    multiplicar = st.form_submit_button('Mul')
    dividir = st.form_submit_button('Div')

if somar:
    st.write(f'### Resultado: {n1 + n2}')
elif subtrair:
    st.write(f'### Resultado: {n1 - n2}')
elif multiplicar:
    st.write(f'### Resultado: {n1 * n2}')
elif dividir:
    st.write(f'### Resultado: {n1 / n2}')