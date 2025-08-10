from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Local PySpark Example") \
    .master("local[*]") \
    .getOrCreate()

# Example DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()

spark.stop()

