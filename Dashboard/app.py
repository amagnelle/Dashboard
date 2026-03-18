import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Dados", layout="wide")

st.title("Dashboard de Análise de Dados")

# Upload do arquivo
arquivo = st.file_uploader("Faça upload do seu arquivo CSV", type=["csv"])

if arquivo:
    df = pd.read_csv(arquivo)

    st.subheader("📌 Dados carregados")
    st.dataframe(df)

    # Converter data
    df['data'] = pd.to_datetime(df['data'])

    # Filtro de data
    data_inicio = st.date_input("Data inicial", df['data'].min())
    data_fim = st.date_input("Data final", df['data'].max())

    df_filtrado = df[(df['data'] >= pd.to_datetime(data_inicio)) & 
                     (df['data'] <= pd.to_datetime(data_fim))]

    # Métricas
    total = df_filtrado['valor'].sum()
    media = df_filtrado['valor'].mean()

    col1, col2 = st.columns(2)
    col1.metric("💰 Total de Vendas", f"R$ {total}")
    col2.metric("📈 Média de Vendas", f"R$ {media:.2f}")

    # Gráfico de barras
    grafico = px.bar(df_filtrado, x="produto", y="valor", color="categoria")
    st.plotly_chart(grafico, use_container_width=True)

    # Gráfico de linha
    grafico2 = px.line(df_filtrado, x="data", y="valor")
    st.plotly_chart(grafico2, use_container_width=True)

    print("Dashboard atualizado com sucesso!")