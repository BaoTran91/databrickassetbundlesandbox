from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame

def find_all_taxis() -> DataFrame:
    return spark.sql("""
    SELECT artist_name, total_number_of_songs, year
    FROM sandbox.tutorial.top_artists_by_year
    WHERE year >= 1990
    ORDER BY total_number_of_songs DESC, year DESC;
    """)

def main():
    find_all_taxis().show(5)

if __name__ == "__main__":
    main()
