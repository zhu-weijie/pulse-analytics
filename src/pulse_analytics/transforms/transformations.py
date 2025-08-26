import pandas as pd


def transform_orders(source_df: pd.DataFrame) -> pd.DataFrame:
    transformed_df = source_df.copy()
    transformed_df = transformed_df.rename(columns={"order_value": "revenue_usd"})
    transformed_df["order_date"] = pd.to_datetime(transformed_df["order_date"])

    print("Transformation successful.")
    return transformed_df
