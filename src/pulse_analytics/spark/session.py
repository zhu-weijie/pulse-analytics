from pyspark.sql import SparkSession


def get_spark_session(app_name: str = "PulseAnalytics") -> SparkSession:
    print("Initializing Spark session...")
    spark = SparkSession.builder.appName(app_name).master("local[*]").getOrCreate()
    print("Spark session initialized successfully.")
    return spark
