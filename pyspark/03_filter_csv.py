###################################################
# Objetivo: Filtrar um arquivo CSV usando PySpark #
###################################################

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
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


df.show()
df.printSchema()
print(f"Total de registros lidos: {df.count()}")

print("############################################################")
df_salario = df \
    .select("nome", "departamento", "salario", "uf") \
    .filter(col("salario") > 15000) \

df_salario.show()
print("Total de funcionários com salário maior que 15.000:",df_salario.count())
print("############################################################")
df_uf = df \
    .select("nome", "departamento", "salario", "uf") \
    .filter(col("uf") == "SP")
df_uf.show()
print("Total de funcionários do estado de SP:",df_uf.count())
print("############################################################")
df_departamento = df \
    .select("nome", "departamento", "salario", "uf") \
    .filter(col("departamento") == "Engenharia") \
    .filter(col("idade") < 30)
df_departamento.show()
print("Total de funcionários do departamento de Engenharia com menos de 30 anos:",df_departamento.count())
print("############################################################")

spark.stop()
