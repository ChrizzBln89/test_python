import os

import yfinance as yf
from pyspark.sql import SparkSession


def main():
    landing_path = os.getenv("LANDING_PATH")
    if not landing_path:
        raise ValueError("Environment variable 'LANDING_PATH' is not set.")

    spark = SparkSession.builder.getOrCreate()

    # Download stock quotes using yfinance
    ticker = "AAPL"
    pandas_df = yf.download(ticker, period="1mo", progress=False)

    if pandas_df.empty:
        raise ValueError(f"No data downloaded for ticker {ticker}")

    # Reset index so that Date / Datetime becomes a regular column
    pandas_df = pandas_df.reset_index()

    # Flatten columns if MultiIndex (e.g. ('Close', 'AAPL') -> 'Close')
    if hasattr(pandas_df.columns, "levels") and len(pandas_df.columns.levels) > 1:
        pandas_df.columns = [col[0] if isinstance(col, tuple) else col for col in pandas_df.columns]

    # Convert all column names to strings for PySpark compatibility
    pandas_df.columns = [str(col) for col in pandas_df.columns]

    # Convert pandas DataFrame to Spark DataFrame
    spark_df = spark.createDataFrame(pandas_df)

    # Save quotes to the landing path using PySpark as CSV
    spark_df.write.mode("overwrite").option("header", "true").csv(landing_path)


if __name__ == "__main__":
    main()
