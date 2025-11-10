from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Primeiro Feitiço") \
    .master("local[*]") \
    .getOrCreate()

dados = [
    ("Alice", 28, "São Paulo"),
    ("Bruno", 35, "Curitiba"),
    ("Carla", 23, "Recife"),
    ("Daniel", 42, "Belo Horizonte"),
    ("Elisa", 31, "Porto Alegre")
]

colunas = ["nome", "idade", "cidade"]

df = spark.createDataFrame(dados, colunas)

df.show()          # mostra os dados
df.printSchema()   # mostra o tipo de cada coluna

df_transformado = df \
    .select("nome", "cidade", "idade") \
    .filter(col("idade") > 30) \
    .withColumn("idade_em_meses", col("idade") * 12)

df_transformado.show()

spark.stop()