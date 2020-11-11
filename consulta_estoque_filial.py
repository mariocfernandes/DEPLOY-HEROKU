import pandas as pd
import streamlit as st

# Titulo
st.title('Consulta Estoque por Coleção - NOV 2020')

opcao_filial  = st.selectbox(
            "Escolha a Filial desejada ",
            (
                "1.Goiabeiras",
                "2.Estação Cuiaba",
                "3.Campo Grande Eldorado",
                "4.GRU - Domestico",
                "5.Santos Dumont"
            )
        )

if opcao_filial == "1.Goiabeiras":
    arquivo = 'goi2020.csv'
elif opcao_filial == "2.Estação Cuiaba":
    arquivo = 'est2020.csv'
elif opcao_filial == "3.Campo Grande Eldorado":
    arquivo = 'cge2020.csv'
elif opcao_filial == "4.GRU - Domestico":
    arquivo = 'gru2020.csv'
elif opcao_filial == "5.Santos Dumont":
    arquivo = 'sdu2020.csv'
    
@st.cache
def get_data():
    return pd.read_csv(arquivo)

df = get_data()

estoque_total = df['Estoque atual'].sum()
            

st.write('Quantidade total de peças...: '+str(estoque_total))

consulta_estoque = df.groupby('Colecao')['Estoque atual'].agg(['sum']).sort_values(by='sum',ascending = False)

st.table(consulta_estoque)

