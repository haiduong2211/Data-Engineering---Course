from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count
from pyspark.sql.window import Window
import time

Start_time = time.time()
# Create spark session
spark = SparkSession \
    .builder \
    .master('local') \
    .appName("DEP303_ASM2_spark") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.3.0") \
    .config("spark.mongodb.read.connection.uri", "mongodb://127.0.0.1:27017/DEP303_asm2") \
    .config("spark.mongodb.write.connection.uri", "mongodb://127.0.0.1:27017/DEP303_asm2") \
    .getOrCreate()

# Load questions collection from MongoDB
questions_df = spark.read \
    .format('mongodb') \
    .option('database', 'DEP303_asm2') \
    .option('collection', 'questions') \
    .load()
#Load answers collection from MongoDB
answers_df = spark.read \
    .format('mongodb') \
    .option('database', 'DEP303_asm2') \
    .option('collection', 'answers') \
    .load()

questions_df.printSchema()
answers_df.printSchema()

### PROCESSING DATA ### 
# Count how many answers each question has
question_answer_count = answers_df.groupBy('parentId').agg(count('Id').alias('answer_count')).select('parentId', 'answer_count')

# Join the question and answer count dataframes
processed_data = questions_df.join(question_answer_count, questions_df.Id == question_answer_count.parentId, 'left').select(questions_df.Id, 'answer_count')
processed_data.show(20)

# Write the processed data to csv folder
processed_data.write.format("csv").mode("overwrite").option("path","/home/airflow/airflow-env/asm2/data/csv/").save()

#quit spark session
spark.stop()
