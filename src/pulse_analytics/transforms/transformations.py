from pyspark.sql import DataFrame
from pyspark.sql.functions import to_date


def transform_orders(source_df: DataFrame) -> DataFrame:
    transformed_df = source_df.withColumnRenamed(
        "order_value", "revenue_usd"
    ).withColumn("order_date", to_date("order_date", "yyyy-MM-dd"))

    print("PySpark transformation successful.")
    return transformed_df
