🧪 Desafio 01 – Criar e Transformar um DataFrame (Modo Aprendiz)
🎯 Objetivo:

Criar um pequeno DataFrame manualmente com PySpark, inspecionar seu schema e aplicar transformações básicas.

📜 Instruções:

Criar uma SparkSession no modo local.

Criar um DataFrame manualmente com os seguintes dados:

nome	|idade	|cidade
|-------|-------|-------|
Alice	|28	    |São Paulo
Bruno	|35	    |Curitiba
Carla	|23	    |Recife
Daniel	|42	    |Belo Horizonte
Elisa	|31	    |Porto Alegre

Exibir:

Os dados com .show()

O schema com .printSchema()

Aplicar transformações:

Selecionar apenas nome e cidade

Filtrar pessoas com idade maior que 30

Adicionar uma nova coluna idade_em_meses (idade * 12)

Salvar o resultado em um novo DataFrame e exibir.

