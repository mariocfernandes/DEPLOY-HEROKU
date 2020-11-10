import pandas as pd
import streamlit as st



# criando um dataframe
#data = pd.read_csv("data.csv")

# título
st.title("Desafio -  Uso do Stremlit")

# subtítulo
st.markdown("Alguns comandos do Streamlit")

# verificando o dataset
st.subheader("Selecionando apenas um pequeno conjunto de atributos")

# atributos para serem exibidos por padrão
#defaultcols = ["RM","PTRATIO","LSTAT","MEDV"]

# defindo atributos a partir do multiselect
#cols = st.multiselect("Atributos", data.columns.tolist(), default=defaultcols)

# exibindo os top 10 registro do dataframe
#st.dataframe(data[cols].head(10))


st.subheader("Exemplo do Slider....")

# definindo a faixa de valores
faixa_valores = st.slider("Faixa Seleçao", min_value=1, max_value=150)

