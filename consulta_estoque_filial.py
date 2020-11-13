import pandas as pd
import streamlit as st

# Titulo
st.title('Consulta Estoque por Filial' )
st.header('Estoques em 13-11-2020')

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
    arquivo = 'goi13112020.csv'
elif opcao_filial == "2.Estação Cuiaba":
    arquivo = 'est13112020.csv'
elif opcao_filial == "3.Campo Grande Eldorado":
    arquivo = 'cge13112020.csv'
elif opcao_filial == "4.GRU - Domestico":
    arquivo = 'gru13112020.csv'
elif opcao_filial == "5.Santos Dumont":
    arquivo = 'sdu13112020.csv'
    
@st.cache
def get_data():
    return pd.read_csv(arquivo)

df = get_data()

estoque_total = df['Estoque atual'].sum()
            

st.write('Quantidade total de peças...: '+str(estoque_total))

consulta_estoque = df.groupby('Colecao')['Estoque atual'].agg(['sum']).sort_values(by='sum',ascending = False)

st.table(consulta_estoque)

st.sidebar.subheader("Visualize os Produtos da Coleção...:")

lista_colecao = df.Colecao.unique().tolist()

escolha_selecao = st.sidebar.selectbox("Escolha a Coleção para visualizar os Produtos",
                                     lista_colecao)

df_filtro = df.Colecao == escolha_selecao

cols = ['Produto','Desc Produto','Desc Cor Produto','Grade','Estoque atual']

st.sidebar.dataframe(df[df_filtro][cols])



