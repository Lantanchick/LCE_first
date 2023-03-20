from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit
from pyspark import SparkContext, SparkConf



spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Tutorial')\
        .getOrCreate()


df_schema = [
               StructField('_c0', IntegerType(), True),
               StructField('symbol', StringType(), True),
               StructField('data', DateType(), True),
               StructField('open', DoubleType(), True),
               StructField('high', DoubleType(), True),
               StructField('low', DoubleType(), True),
               StructField('close', DoubleType(), True),
               StructField('volume', IntegerType(), True),
               StructField('adjusted', DoubleType(), True),
               StructField('market.cap', StringType(), True),
               StructField('sector', StringType(), True),
               StructField('industry', StringType(), True),
               StructField('exchange', StringType(), True),
            ]

df_true = StructType(fields = df_schema)

# url = "https://www.dropbox.com/s/ru96yt1m92xdltx/stocks_price_final.csv?dl=1"  ссылка на файл
url = "db_folder/DB_file.csv"

df = spark.read.csv(
    url,
    sep=',',
    header=True,
    schema=df_true
)

# функции обработки
def getDF(start_data = False, end_data = False, industry = False, DF = df ):
    if start_data and end_data:
        DF = DF.filter( 
            (col('data') >= lit(start_data)) & 
            (col('data') <= lit(end_data)) 
            )
    if industry:
        DF = DF.filter(
            col('industry') == industry
            )
    return DF

def getInd():
    return df.select("industry").distinct()

