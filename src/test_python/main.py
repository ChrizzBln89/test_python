import argparse

from pyspark.sql import SparkSession

from test_python import taxis


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--schema", required=True)
    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()
    spark.sql(f"USE CATALOG `{args.catalog}`")
    spark.sql(f"USE SCHEMA `{args.schema}`")

    taxis.find_all_taxis().show(5)


if __name__ == "__main__":
    main()
