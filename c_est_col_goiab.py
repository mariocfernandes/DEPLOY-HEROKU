import pandas as pd
import streamlit as st

@st.cache
def get_data():
    return pd.read_csv('goi2020.csv')

df = get_data()

estoque_total = df['Estoque atual'].sum()

# Titulo
st.title('Consulta Estoque por Coleção - Goiabeiras/NOV2020')

st.write('Quantidade total de peças...: '+str(estoque_total))

consulta_estoque = df.groupby('Colecao')['Estoque atual'].agg(['sum']).sort_values(by='sum',ascending = False)

st.dataframe(consulta_estoque)
