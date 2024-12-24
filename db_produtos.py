import csv
from faker import Faker

fake = Faker('pt_BR')  # Gerar dados 

# Criar lista para armazenar dados
produtos = []

# Gerar 1000 registros
for _ in range(1000):
    produto = {
        'id': fake.uuid4(),
        'nome': fake.name(),
        'descricao': fake.paragraph(),
        'preco': fake.random_number(digits=4),
        'categoria': fake.random_element(['Eletrônicos', 'Vestuário', 'Beleza'])
    }
    produtos.append(produto)

# Exportar para um arquivo CSV
with open('produtos.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'nome', 'descricao', 'preco', 'categoria']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(produtos)

#

