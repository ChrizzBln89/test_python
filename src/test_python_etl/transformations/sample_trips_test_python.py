from pyspark import pipelines as dp

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def sample_trips_test_python():
    # Ensure spark.config is available as an alias for spark.conf
    if hasattr(spark, "conf") and not hasattr(spark, "config"):  # noqa: F821
        spark.config = spark.conf  # noqa: F821

    # Get configuration from pipeline YAML configuration with spark.config.get
    target_catalog = spark.config.get("TARGET_CATALOG", "samples")  # noqa: F821
    target_schema = spark.config.get("TARGET_SCHEMA", "nyctaxi")  # noqa: F821

    return spark.read.table(f"{target_catalog}.{target_schema}.trips")  # noqa: F821
