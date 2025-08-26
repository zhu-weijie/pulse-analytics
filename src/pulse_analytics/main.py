from pulse_analytics.spark.session import get_spark_session
from pulse_analytics.transforms.transformations import transform_orders


def main():
    print("Starting the Spark transformation process...")

    spark = get_spark_session(app_name="PulseAnalyticsTransform")

    try:
        input_filepath = "/app_data/raw/orders.csv"

        raw_df = spark.read.csv(input_filepath, header=True, inferSchema=True)
        print(f"Successfully loaded data from {input_filepath}")
        print("Raw data schema:")
        raw_df.printSchema()
        print("Raw data:")
        raw_df.show()

        transformed_df = transform_orders(raw_df)

        print("Transformed data schema:")
        transformed_df.printSchema()
        print("Transformed data:")
        transformed_df.show()

    finally:
        print("Stopping Spark session...")
        spark.stop()
        print("Spark session stopped.")

    print("Transformation process finished.")


if __name__ == "__main__":
    main()
