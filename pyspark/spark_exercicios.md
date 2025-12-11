### 🧪 Card 01 – Ler dados de funcionários

**Objetivo:** Carregar um arquivo CSV contendo informações de funcionários.

**Arquivo de origem:** `funcionarios.csv`

**Colunas esperadas:**
- id (int)
- nome (string)
- idade (int)
- departamento (string)
- salario (float)
- admissao (data)
- uf (string - 2 letras)

**Tarefas:**
- [X] Criar schema manual com tipos corretos
- [X] Ler o arquivo CSV aplicando o schema
- [X] Exibir os dados com `.show()` e o schema com `.printSchema()`

**Dificuldade:** 🟢 Fácil
**Tempo estimado:** 15 min

### 🧪 Card 02 – Filtros e Seleções Específicas

**Objetivo:** Aplicar filtros e seleções no DataFrame de funcionários para realizar análises pontuais.

**Arquivo de origem:** `funcionarios.csv`

**Colunas disponíveis:**
- id (int)
- nome (string)
- idade (int)
- departamento (string)
- salario (float)
- admissao (data)
- uf (string)

**Tarefas:**
- [X] Selecionar apenas `nome`, `departamento`, `salario` e `uf`
- [X] Filtrar funcionários com salário maior que 15.000
- [X] Filtrar funcionários do estado de "SP"
- [X] Filtrar funcionários do departamento "Engenharia" com idade menor que 30
- [X] Exibir os resultados com `.show()`

**Bônus:**
- [X] Contar quantos funcionários atendem cada filtro com `.count()`
- [X] Encadear dois filtros seguidos no mesmo comando (ex: `.filter(...).filter(...)`)

**Dificuldade:** 🟢 Fácil  
**Tempo estimado:** 20 min

### 🧪 Card 03 – Transformações com `.withColumn()` e lógica condicional

**Objetivo:** Criar novas colunas com base em cálculos e regras de negócio simples, utilizando `.withColumn()` e funções do PySpark.

**Arquivo de origem:** `funcionarios.csv`

**Colunas disponíveis:**
- id (int)
- nome (string)
- idade (int)
- departamento (string)
- salario (float)
- admissao (data)
- uf (string)

**Tarefas:**
- [X] Criar uma nova coluna `salario_anual` multiplicando o salário por 12
- [X] Criar a coluna `idade_em_meses` multiplicando idade por 12
- [X] Criar a coluna `senioridade` com as regras:
  - "Junior" se idade < 30
  - "Pleno" se idade entre 30 e 45
  - "Senior" se idade > 45
- [X] Mostrar 10 linhas com `.show(truncate=False)`

**Bônus:**
- [X] Usar `.alias()` para renomear colunas durante seleção
- [X] Mostrar quantos funcionários há em cada faixa de `senioridade` com `.groupBy().count()`

**Dificuldade:** 🟡 Médio  
**Tempo estimado:** 30 minutos

### 🧪 Card 04 – Trabalhando com Datas e Ordenações

**Objetivo:** Manipular e explorar dados temporais para análises históricas e ordenações.

**Arquivo de origem:** `funcionarios.csv`

**Colunas disponíveis:**
- admissao (data)

**Tarefas:**
- [X] Criar uma nova coluna `ano_admissao` extraindo o ano da data
- [X] Criar a coluna `tempo_empresa_meses` calculando diferença em meses até hoje
- [X] Ordenar os funcionários por data de admissão (mais antigos primeiro)
- [X] Exibir os 10 funcionários mais antigos da empresa com `.show(truncate=False)`

**Bônus:**
- [X] Agrupar por `ano_admissao` e contar quantos funcionários foram admitidos por ano
- [X] Encontrar o funcionário mais novo da empresa (por `admissao`) com `.orderBy().limit(1)`

**Dificuldade:** 🟡 Médio  
**Tempo estimado:** 30 min
