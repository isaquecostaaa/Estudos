# 4) Carregue adequadamente o dataset Adult Income (disponível para download) e exiba as primeiras 3 linhas.
#%%
import pandas as pd

df = pd.read_csv("adult.csv")
print(df.head(3))


# 5) Quantas linhas e colunas existem no dataset?
#%%
import pandas as pd

df = pd.read_csv('adult.csv')

linhas, colunas = df.shape

print(f'O dataset tem {linhas} linhas e {colunas} colunas.')

# 6) Quais colunas possuem valores ausentes? Qual a porcentagem de valores ausentes em cada uma?
#%%
import pandas as pd

df = pd.read_csv('adult.csv')

df.replace('?', pd.NA, inplace=True)

colunas_ausentes = df.isnull().sum()
percent_ausentes = (colunas_ausentes / len(df)) * 100

if colunas_ausentes.sum() > 0:
    for coluna, ausentes, percent in zip(colunas_ausentes.index, colunas_ausentes, percent_ausentes):
        if ausentes > 0:
            print(f'Coluna: {coluna} - Ausentes: {ausentes} ({percent:.2f}%)')
else:
    print("Não há valores ausentes ou com '?' no dataset.")


# 7) Quantas categorias diferentes existem na coluna "workclass"?
# %%
import pandas as pd

df = pd.read_csv('adult.csv')

num_categorias = df['workclass'].nunique()

print(f'A coluna "workclass" possui {num_categorias} categorias diferentes.')

# 8) Quantas pessoas do dataset possuem nível de educação "Bachelors"?
#%%

import pandas as pd

df = pd.read_csv('adult.csv')

num_bachelors = df[df['education'] == 'Bachelors'].shape[0]

print(f'O número de pessoas com nível de educação "Bachelors" é {num_bachelors}.')

# 9) Qual é a média de horas trabalhadas por semana ("hours-per-week") para quem ganha mais de $50K e para quem ganha menos?
# %%

import pandas as pd

df = pd.read_csv('adult.csv')

maior_50K = df[df['income'] == '>50K']
menor_50K = df[df['income'] == '<=50K']

media_maior_50K = maior_50K['hours-per-week'].mean()
media_menor_50K = menor_50K['hours-per-week'].mean()

print(f'Média de horas trabalhadas por semana para quem ganha mais de $50K: {media_maior_50K:.2f}')
print(f'Média de horas trabalhadas por semana para quem ganha $50K ou menos: {media_menor_50K:.2f}')


# 10) Quais são as 3 ocupações ("occupation") mais comuns entre pessoas que ganham mais de $50K?
# %%

import pandas as pd

df = pd.read_csv('adult.csv')

maior_50K = df[df['income'] == '>50K']

top_3_ocupacoes = maior_50K['occupation'].value_counts().head(3)

print('As 3 ocupações mais comuns entre pessoas que ganham mais de $50K:')
print(top_3_ocupacoes)


# 11) Extraia apenas a primeira palavra da coluna "education", criando uma nova coluna "education_first_word".
# %%

import pandas as pd

df = pd.read_csv('adult.csv')

df['education_first_word'] = df['education'].str.split(r'\W+').str[0]

print(df[['education', 'education_first_word']].head())

# 12) Filtre apenas os dados de mulheres que trabalham mais de 40 horas por semana.
# %%
import pandas as pd

df = pd.read_csv('adult.csv')
filtered_df = df[(df['gender'] == 'Female') & (df['hours-per-week'] > 40)]

print(filtered_df)


# 13) Ordene o DataFrame pelo salário ("income") e depois pela idade ("age"), do maior para o menor.

# %%
import pandas as pd

df = pd.read_csv('adult.csv')

sorted_df = df.sort_values(by=['income', 'age'], ascending=[False, False])

print(sorted_df)

# 14) Crie uma nova coluna "capital_difference", que é a diferença entre "capital-loss" e "capital-gain".
# %%
import pandas as pd

df = pd.read_csv('adult.csv')

df['capital_difference'] = df['capital-loss'] - df['capital-gain']

print(df[['capital-loss', 'capital-gain', 'capital_difference']])

# 15) Crie uma nova coluna "age_decade" que indica em qual década a pessoa nasceu (Exemplo: se a idade é 37, então "age_decade"="30s").
# %%
import pandas as pd

df = pd.read_csv('adult.csv')

df['age_decade'] = (df['age'] // 10) * 10
df['age_decade'] = df['age_decade'].astype(str) + 's'

print(df[['age', 'age_decade']])

# 16)Crie uma nova coluna "marital_status_code" que converte "marital-status" em variáveis numéricas (0, 1, 2, … para cada classe diferente)
#%%
import pandas as pd

df = pd.read_csv('adult.csv')

df['marital_status_code'] = df['marital-status'].astype('category').cat.codes

print(df[['marital-status', 'marital_status_code']])

# %%
