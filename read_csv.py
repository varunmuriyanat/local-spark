from pyspark.sql import SparkSession
from pyspark.sql.functions import year, to_date

# Create Spark session
spark = SparkSession.builder \
    .appName("Local PySpark Example") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("customers_100.csv", header=True, inferSchema=True)

# 'DateJoined' is in 'yyyy-MM-dd' format
df = df.withColumn("year", year(to_date(df["DateJoined"])))

df.show()

# Write to Parquet, partitioned by
df.write.partitionBy("year").parquet("customers_parquet", mode="overwrite")

spark.stop()