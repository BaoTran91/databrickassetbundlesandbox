from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame

def load_top_artists_by_year() -> DataFrame:
    return spark.sql("""
    SELECT *
    FROM sandbox.tutorial.top_artists_by_year
    WHERE year >= 1990
    ORDER BY total_number_of_songs DESC, year DESC;
    """)

def main():
    load_top_artists_by_year().show(5)

if __name__ == "__main__":
    main()
