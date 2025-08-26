import pandas as pd

from pulse_analytics.transforms.transformations import transform_orders


def main():
    print("Starting the transformation process...")
    input_filepath = "/app_data/raw/orders.csv"

    try:
        raw_df = pd.read_csv(input_filepath)
        print(f"Successfully loaded data from {input_filepath}")
        print("Raw data:")
        print(raw_df.head())
    except FileNotFoundError:
        print(f"Error: Could not find the file at {input_filepath}")
        print("Please ensure the data volume is correctly mounted.")
        return

    transformed_df = transform_orders(raw_df)

    print("\nTransformed data:")
    print(transformed_df.head())
    print("\nTransformed data types:")
    print(transformed_df.info())

    print("\nTransformation process finished.")


if __name__ == "__main__":
    main()
