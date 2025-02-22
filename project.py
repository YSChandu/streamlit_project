import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("📊 Correlation Heatmap of CSV Data")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("### Preview of Data")
    st.dataframe(df.head())

    numeric_df = df.select_dtypes(include=['number'])

    correlation_matrix = numeric_df.corr()

    st.write("### Correlation Matrix")
    st.dataframe(correlation_matrix)

    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
    st.pyplot(fig)
