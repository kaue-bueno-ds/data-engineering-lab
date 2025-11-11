Para iniciar o spark:
```
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Primeiro Feitiço") \
    .master("local[*]") \
    .getOrCreate()
```

Explicação:
- `appName("Primeiro Feitiço")`: só nome que aparece no log da aplicação;
- `master(local[*])`: utiliza todos os núcleos do PC;
- `.getOrCreate()`: cria a sessão se ela não existir ainda;

Toda sessão Spark deve ser finalizada com um .stop(), ou ela vagará pelos processos como um espectro faminto. 

```
spark.stop()
```

Para criar um DataFrame manual:
```
dados = [
    ("Kauê", 28, "SP"),
    ("Bruna", 35, "PR")
]

colunas = ["nome", "idade", "uf"]

df = spark.createDataFrame(dados, colunas)
```

- `dados`: lista de tuplas, cada tupla é uma linha do DataFrame.
- `colunas`: nomes das colunas, na mesma ordem dos dados.
- O Spark infere automaticamente os tipos das colunas (inteiro, string, etc).
- `df.show()` exibe os dados.
- `df.printSchema()` mostra os tipos de cada coluna.

Para criar um schema manual (explícito), útil quando queremos forçar tipos:
```
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("nome", StringType(), True),
    StructField("idade", IntegerType(), True),
    StructField("uf", StringType(), True)
])

df = spark.createDataFrame(dados, schema=schema)
```

- Aqui usamos `StructType` e `StructField` para definir nome, tipo e se pode ser nulo.
- `StringType()` não limita o tamanho (não tem VARCHAR(2) como no SQL), mas representa texto.

Transformações no DataFrame (imutáveis):
```
from pyspark.sql.functions import col

df_transformado = df \
    .select("nome", "cidade", "idade") \
    .filter(col("idade") > 30) \
    .withColumn("idade_em_meses", col("idade") * 12)

df_transformado.show()
```

- `select()`: escolhe colunas.
- `filter()`: aplica condição como um WHERE.
- `withColumn()`: cria nova coluna com base em uma existente.
- Cada operação retorna um **novo** DataFrame (Spark é imutável).
- O operador `\` permite quebrar a linha no Python, apenas para legibilidade.

Para análises pontuais:
```
df.filter(col("nome") == "Kauê").show()
```

- Muito usado para debug e validação durante construção do pipeline.
