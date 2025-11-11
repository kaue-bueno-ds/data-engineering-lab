import pandas as pd
import random
from faker import Faker
from datetime import datetime
from tqdm import tqdm

fake = Faker('pt_BR')
random.seed(42)

# Número de registros a serem gerados
n = 1_000_000

# Departamentos e UFs simuladas
departamentos = ['Engenharia', 'RH', 'Marketing', 'Financeiro', 'Vendas', 'TI']
ufs = ['SP', 'RJ', 'MG', 'PR', 'RS', 'SC', 'BA', 'PE', 'CE', 'GO']

# Função para gerar dados
def gerar_dados():
    return {
        "id": random.randint(1000, 9999),
        "nome": fake.name(),
        "idade": random.randint(18, 65),
        "departamento": random.choice(departamentos),
        "salario": round(random.uniform(3000, 20000), 2),
        "admissao": fake.date_between(start_date='-15y', end_date='today').strftime('%Y-%m-%d'),
        "uf": random.choice(ufs)
    }

# Gerar DataFrame
dados = [gerar_dados() for _ in tqdm(range(n))]
df = pd.DataFrame(dados)

# Salvar como CSV
df.to_csv("funcionarios.csv", index=False)