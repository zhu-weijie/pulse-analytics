from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date


def transform_orders(source_df: DataFrame) -> DataFrame:
    transformed_df = source_df

    transformed_df = transformed_df.withColumnRenamed("order_value", "revenue_usd")

    transformed_df = transformed_df.withColumn(
        "order_date", to_date(col("order_date"), "yyyy-MM-dd")
    )

    print("PySpark transformation successful.")
    return transformed_df
