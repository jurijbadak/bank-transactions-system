from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Spark Session erstellen
spark = SparkSession.builder \
    .appName("BankTransactionsStreaming") \
    .master("local[*]") \
    .getOrCreate()

# Kafka-Stream lesen
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank-transactions") \
    .load()

# Nachrichten deserialisieren
df = df.selectExpr("CAST(value AS STRING)")

# Einfache Transformationen oder Aggregationen durchführen
# Beispiel: Zählen der Transaktionen nach Typ
aggregated_df = df.groupBy("type").count()

# Ausgabe in der Konsole
query = aggregated_df \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()