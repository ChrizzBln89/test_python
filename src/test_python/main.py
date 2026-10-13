import os
from pyspark.sql import SparkSession
from test_python import taxis


def main():
    catalog = os.getenv("TARGET_CATALOG")
    schema = os.getenv("TARGET_SCHEMA")
    if not catalog or not schema:
        raise ValueError("Environment variables 'TARGET_CATALOG' and 'TARGET_SCHEMA' must be set.")

    spark = SparkSession.builder.getOrCreate()
    spark.sql(f"USE CATALOG `{catalog}`")
    spark.sql(f"USE SCHEMA `{schema}`")

    # Example: just find all taxis from a sample catalog
    taxis.find_all_taxis().show(5)


if __name__ == "__main__":
    main()
