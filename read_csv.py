from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Local PySpark Example") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("customers_100.csv")

df.show()

spark.stop()

