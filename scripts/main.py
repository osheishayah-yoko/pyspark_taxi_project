
from pyspark.sql import SparkSession

def create_spark_session(app_name="PySparkTaxiProject"):
    """Creates and returns a SparkSession."""
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark

def load_data(spark, file_path):
    """Loads the CSV data into a Spark DataFrame."""
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    print(f"Data loaded from {file_path}. Schema:")
    df.printSchema()
    print("First 5 rows:")
    df.show(5)
    return df

if __name__ == "__main__":
    spark = create_spark_session()
    data_path = "/home/ubuntu/pyspark_taxi_project/data/yellow_tripdata_2016-03.csv"
    taxi_df = load_data(spark, data_path)

    # Stop the SparkSession
    spark.stop()

