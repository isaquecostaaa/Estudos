import pandas as pd

try:
    df = pd.read_csv("superstore.csv", encoding='latin1')

    categorias = df["Category"].unique()

    with pd.ExcelWriter("relatorio_vendas_por_categoria.xlsx") as writer:
        for categoria in categorias:
            df_categoria = df[df["Category"] == categoria]
            resumo_categoria = df_categoria.groupby("Sub-Category")["Sales"].sum().reset_index()

            resumo_categoria.to_excel(writer, sheet_name=categoria, index=False)
    
    print("Relatório gerado com sucesso! O arquivo 'relatorio_vendas_por_categoria.xlsx' foi criado.")

except FileNotFoundError:
    print("Erro: O arquivo 'superstore.csv' não foi encontrado. Verifique o caminho e tente novamente!")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio. Verifique o conteúdo do arquivo!")
except pd.errors.ParserError:
    print("Erro: Problema ao ler o arquivo. Verifique se ele está formatado corretamente!")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
