from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, sum, split, explode, col, array_distinct, lower, expr, regexp_extract_all,lit, regexp_extract,count, date_format, to_date
from pyspark.sql.window import Window
import time

Start_time = time.time()

# Create spark session
spark = SparkSession \
    .builder \
    .master('local') \
    .appName("myApp") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.3.0") \
    .config("spark.mongodb.read.connection.uri", "mongodb://127.0.0.1:27017/DEP303_ASM1") \
    .config("spark.mongodb.write.connection.uri", "mongodb://127.0.0.1:27017/DEP303_ASM1") \
    .getOrCreate()

# Load QUESTIONS data from MongoDB
questions_df = spark.read \
    .format('mongodb') \
    .option('database', 'DEP303_ASM1') \
    .option('collection', 'Questions') \
    .load()

# Convert CreationDate,ClosedDate to timestamp
questions_df = questions_df.withColumn("CreationDate", to_timestamp(col("CreationDate")))
questions_df = questions_df.withColumn("ClosedDate", to_timestamp(col("ClosedDate")))

#Convert OwnerUserId to integer type, replacing NA with NULL
questions_df = questions_df.withColumn("OwnerUserId", when(col("OwnerUserId")=='NA',None).otherwise(col("OwnerUserId")).cast("integer"))

print("Questions Schema:")
questions_df.printSchema()


#Load ANSWERS data from MongoDB
answers_df = spark.read \
    .format('mongodb') \
    .option('database', 'DEP303_ASM1') \
    .option('collection', 'Answers') \
    .load()

#Convert CreateDate to timestamp - answers
answers_df = answers_df.withColumn("CreationDate", to_timestamp(col("CreationDate")))

#Convert OwnerUserId to integer type, replacing NA with NULL - answers
answers_df = answers_df.withColumn("OwnerUserId", when(col("OwnerUserId")=='NA',None).otherwise(col("OwnerUserId")).cast("integer"))

print('Answers Schema:')
answers_df.printSchema()

#Start time tracking
Read_data_time = time.time()
##############################################
### REQUEST 1 ### Calculate the programming language used in the questions
print("=== REQUEST 1 ===")
print("Tính ngôn ngữ lập trình được sử dụng trong các câu hỏi") 
# Create a regex pattern that matches any of the languages
pattern = r"(" + r"Java|Python|C\\+\\+|C\\#|Go|Ruby|Javascript|PHP|HTML|CSS|SQL" + r")"

# Extract all matches of the pattern from the 'Body' column
df = questions_df.withColumn('Languages', expr(f"regexp_extract_all(Body, '{pattern}')"))

# Explode the 'Languages' column into multiple rows
df = df.select('*', explode(df.Languages).alias('Programming_Language'))

# Aggregate the count of each language
language_counts = df.groupBy('Programming_Language').count()
language_counts.show(10)  
Request1_time = time.time()

##############################################
### REQUEST 2 ### Find the most used domain in the questions
print("=== REQUEST 2 ===")
print("Tìm domain được sử dụng nhiều nhất trong các câu hỏi")
# Extract the domain from the 'Body' column
url_pattern = r'https?://(?:[-\w]+\.)+[-\w]+[^ ]*' # regex pattern for URL
questions_df2 = questions_df.select('Body')
url_df = questions_df2.withColumn('Domain', regexp_extract('Body', url_pattern, 0))

#remove head and tail of the URL
url_df = url_df.withColumn('Domain', regexp_extract('Domain', r'(https?://)?(www\.)?(.+?)(/|$)', 3))
url_df = url_df.filter((url_df.Domain.isNotNull()) & (col('Domain') != '') & (col('Domain') != 'http:'))

#count the number of each domain
domain_counts = url_df.groupBy('Domain').count()
#sort the domain by count
domain_counts = domain_counts.orderBy(col('count').desc())
domain_counts.show(10)

Request2_time=time.time()

##############################################
### REQUEST 3 ### Calculate the total score of User by day
print("=== REQUEST 3 ===")
print("Tính tổng điểm của người dùng theo ngày")
# Window specification
windowSpec = Window.partitionBy("OwnerUserId",col('CreationDate').cast('date')).orderBy(col("CreationDate").cast('date')).rowsBetween(Window.unboundedPreceding, 0)

# Calculate the cumulative sum of the 'Score' column
questions_df3 = questions_df.withColumn('TotalScore', sum('Score').over(windowSpec))
questions_df3 = questions_df3.filter(questions_df3.OwnerUserId.isNotNull())
questions_df3 = questions_df3.select('OwnerUserId',col('CreationDate').cast('date'),'TotalScore')
questions_df3.show(10)

request3_time = time.time()

##############################################
### REQUEST 4 ### Calculate the total score of User time period
print("=== REQUEST 4 ===")
print("Tính tổng điểm của người dùng trong một khoảng thời gian")
START = '2008-01-01'
END = '2009-01-01'
print(f'StartDate:{START}, EndDate:{END}')
filtered_df = questions_df3.filter((col('CreationDate') >= START) & (col('CreationDate') < END))
result = filtered_df.groupBy('OwnerUserId').agg(sum('TotalScore').alias('TotalScore'))
result.show(5)

request4_time = time.time()

##############################################
### REQUEST 5 ### Find the question that have more than 5 answers
print("=== REQUEST 5 ===")
print("Tìm các câu hỏi có nhiều hơn 5 câu trả lời")
joined_df = questions_df.join(answers_df, questions_df.Id == answers_df.ParentId, 'left').select(questions_df.OwnerUserId,questions_df.Id,answers_df.ParentId,answers_df.Id.alias("AnswersId"),questions_df.CreationDate.alias('QuestionDate'),answers_df.CreationDate.alias('AnswerDate'))

# print('### JOINED_DF SCHEMA ###')
# joined_df.printSchema()

grouped_df = joined_df.groupBy(joined_df.Id).agg(count('AnswersID').alias('AnswerCount'))
filtered_df = grouped_df.filter(col('AnswerCount') > 5)
filtered_df.show(5)

request5_time = time.time()

##############################################
### REQUEST 6 ### Find Active Users
print("=== REQUEST 6 ===")
print("Tìm các Active User")

# Filter active users based on the number of questions >50
active_users1 = answers_df.groupBy('OwnerUserId').agg(count('Id').alias('AnswerCount')).filter(col('AnswerCount') > 50).select('ownerUserId')

# Filter active users based on the total score >500
active_users2 = answers_df.groupBy('OwnerUserId').agg(sum('Score').alias('TotalScore')).filter(col('TotalScore') > 500).select('ownerUserId')

# print('active_user1,2 schema:')
# active_users1.printSchema()
# active_users2.printSchema()

# Using Request 5 joined_df dataframe to filter the answers on the same day as the questions
joined_df2 = joined_df.filter(date_format(joined_df.QuestionDate, 'yyyy-MM-dd') == date_format(joined_df.AnswerDate, 'yyyy-MM-dd'))
# print('Joined_df2 Schema')
# joined_df2.printSchema()

# Count the number of answers on the same day the question created for each user
active_users3 = joined_df2.groupBy('OwnerUserId').agg(count('Id').alias('SameDayAnswerCount')).filter(col('SameDayAnswerCount') > 5).select('OwnerUserId')
# print('active_user3 schema:')
# active_users3.printSchema()
active_users = active_users1.union(active_users2).union(active_users3).distinct()

active_users.show(5)

request6_time = done_time = time.time()


##############################################
# Show time data
# Show time data with formatted output
print("Read data time: {:.2f} seconds".format(Read_data_time - Start_time))
print("Request 1 time: {:.2f} seconds".format(Request1_time - Read_data_time))
print("Request 2 time: {:.2f} seconds".format(Request2_time - Request1_time))
print("Request 3 time: {:.2f} seconds".format(request3_time - Request2_time))
print("Request 4 time: {:.2f} seconds".format(request4_time - request3_time))
print("Request 5 time: {:.2f} seconds".format(request5_time - request4_time))
print("Request 6 time: {:.2f} seconds".format(request6_time - request5_time))
print("Total time: {:.2f} seconds".format(done_time - Start_time))
