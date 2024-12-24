from faker import Faker
import pandas as pd

fake = Faker()

# Gerando um DataFrame com dados de vendas fake
dados_vendas = {
    'Data': [fake.date_this_year() for _ in range(100)],
    'Produto': [fake.word() for _ in range(100)],
    'Quantidade': [fake.random_number(digits=3) for _ in range(100)],
    'Preço': [fake.random_number(digits=4) for _ in range(100)]
}

df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas.head())
