###################################################
# Objetivo: Filtrar um arquivo CSV usando PySpark #
###################################################

from pyspark.sql import SparkSession
from pyspark.sql.functions import col,when,year,month,current_date, datediff,months_between, round,asc,desc
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
    ,col("admissao")
    ,(year(col("admissao"))).alias("ano_admissao")
    ) \
    .withColumn("tempo_empresa_meses", round(months_between(current_date(), col("admissao")),0)) \
    
df_ordernado_asc = df_transformado.orderBy(asc("admissao"))
df_ordernado_asc.show(truncate=False)

df_transformado.groupBy("ano_admissao").count().show()

df_ordernado_desc = df_transformado.orderBy(desc("admissao")).limit(1)
df_ordernado_desc.show()

spark.stop()
