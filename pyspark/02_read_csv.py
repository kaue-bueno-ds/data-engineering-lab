#################################################
# Objetivo: Ler um arquivo CSV usando PySpark  #
#################################################

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
spark.stop()
