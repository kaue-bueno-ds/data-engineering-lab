###################################################
# Objetivo: Filtrar um arquivo CSV usando PySpark #
###################################################

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, DateType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("nome", StringType(), True),
    StructField("idade", IntegerType(), True),
    StructField("departamento", StringType(), True),
    StructField("salario", DecimalType(10,2), True),
    StructField("admissao", DateType(), True),
    StructField("uf", StringType(), True),
])

spark = SparkSession.builder \
    .appName("Leitura de CSV") \
    .master("local[*]") \
    .getOrCreate()

path = 'funcionarios.csv'

df = spark.read.format("csv") \
    .option("header", True) \
    .option("mode", "DROPMALFORMED") \
    .schema(schema) \
    .load(path)

df_transformado = df.select(
     col("nome")
    ,col("departamento")
    ,col("idade")
    ,col("salario")
    ,col("uf")
    ,(col("salario")*12).alias("salario_anual")
    ,(col("idade")*12).alias("idade_em_meses")
    ) \
    .withColumn("senioridade", \
    when(col("idade") < 30, "Junior") \
    .when(((col("idade") >= 30) & (col("idade") <= 45)), "Pleno") \
    .when(col("idade") > 45, "Senior"))
df_transformado.show(truncate=False)

df_transformado.groupBy("senioridade").count().show()

spark.stop()