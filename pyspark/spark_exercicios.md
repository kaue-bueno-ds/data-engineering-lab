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
- [ ] Selecionar apenas `nome`, `departamento`, `salario` e `uf`
- [ ] Filtrar funcionários com salário maior que 15.000
- [ ] Filtrar funcionários do estado de "SP"
- [ ] Filtrar funcionários do departamento "Engenharia" com idade menor que 30
- [ ] Exibir os resultados com `.show()`

**Bônus:**
- [ ] Contar quantos funcionários atendem cada filtro com `.count()`
- [ ] Encadear dois filtros seguidos no mesmo comando (ex: `.filter(...).filter(...)`)

**Dificuldade:** 🟢 Fácil  
**Tempo estimado:** 20 min

