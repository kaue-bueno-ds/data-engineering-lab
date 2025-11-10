Para iniciar o spark:
```
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Primeiro Feitiço") \
    .master("local[*]") \
    .getOrCreate()
```
Explicação:
- ```appName("Primeiro Feitiço")```: só nome que aparece no log da aplicação;
- ```master(local[*])```: utiliza todos os núcleos do PC;
- ```.getOrCreate()```: cria a sessão se ela não existir ainda;

Toda sessão Spark deve ser finalizada com um .stop(), ou ela vagará pelos processos como um espectro faminto. 

```spark.stop()```