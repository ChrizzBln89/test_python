from pyspark import pipelines as dp


@dp.table
def sample_trips_test_python():
    if hasattr(spark, "conf") and not hasattr(spark, "config"):  # noqa: F821
        spark.config = spark.conf  # noqa: F821

    catalog = spark.config.get("TARGET_CATALOG", "samples")  # noqa: F821
    schema = spark.config.get("TARGET_SCHEMA", "nyctaxi")  # noqa: F821

    return spark.read.table(f"{catalog}.{schema}.trips")  # noqa: F821
