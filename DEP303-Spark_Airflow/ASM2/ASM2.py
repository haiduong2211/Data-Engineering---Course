from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

from google_drive_downloader import GoogleDriveDownloader as gdd
import os

from datetime import datetime

folder_path = '/home/airflow/airflow-senv/asm2/data/'
## FUNCTIONS ## 

def branching():
    #Check if the file is downloaded
    if os.listdir(folder_path): #If the folder is not empty
        return 'clear_files'
    else:
        print("Folder is already empty.")
        return 'end'

# Clear the Questions.csv and Answers.csv in the folder
def clear_files():
    for file in os.listdir(folder_path):
        if file == 'Questions.csv' or file =='Answers.csv':
            file_path = os.path.join(folder_path,file)
            os.remove(file_path)
        else:
            continue
    print("Files cleared.")
        

def download_question_file():
    gdd.download_file_from_google_drive(file_id='1HuN_aQdhXjXO_4EMHAWqx9kZKejdxdTt',dest_path=folder_path+'Questions.csv',showsize=True,overwrite=True)    # Download the file to the folder_path, overwrite to make sure the file is updated
    print("Question File downloaded.")

def download_answer_file():
    gdd.download_file_from_google_drive(file_id='19S4HicaXWE32M9Jk_wfIQYJgVg4RW-p6',dest_path=folder_path+'Answers.csv',showsize=True,overwrite=True)    # Download the file to the folder_path, overwrite to make sure the file is updated
    print("Answer file downloaded.")

## Create the DAG
with DAG('asm2_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily',catchup=False) as dag:
    start = DummyOperator(task_id='start')

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=branching
    )

    clear_files = PythonOperator(
        task_id='clear_files',
        python_callable=clear_files
    )

    download_question_file_task = PythonOperator(
        task_id='download_question_file',
        python_callable=download_question_file
    )

    download_answer_file_task = PythonOperator(
        task_id='download_answer_file',
        python_callable=download_answer_file
    )
    
    #import data to mongo using BashOperator and mongoimport
    import_questions_mongo = BashOperator(
        task_id='import_questions_mongo',
        bash_command='mongoimport --db DEP303_asm2 --collection questions --type csv --headerline --file /home/airflow/airflow-env/asm2/data/Questions.csv'
    )

    import_answers_mongo = BashOperator(
        task_id='import_answers_mongo',
        bash_command='mongoimport --db DEP303_asm2 --collection answers --type csv --headerline --file /home/airflow/airflow-env/asm2/data/Answers.csv'
    )
    
    # Spark Process - Aggregate the total number of answers for each question and save to csv folder
    spark_process = SparkSubmitOperator(
        task_id='spark_process',
        application='/home/airflow/airflow-env/asm2/spark_process.py',
        conn_id='spark_local',
        packages='org.mongodb.spark:mongo-spark-connector_2.12:10.3.0'
    )

    # Import the output csv to mongo. Import every csv file in csv folder
    import_output_mongo = BashOperator(
        task_id='import_output_mongo',
        bash_command='for file in /home/airflow/airflow-env/asm2/data/csv/*.csv; do ' 'mongoimport --db DEP303_asm2 --collection output --type csv --headerline --file "$file"; ' 'done'
    )

    end = DummyOperator(task_id='end')


start >> branching >>clear_files >> [download_answer_file_task, download_question_file_task]
branching >> end

download_answer_file_task >> import_answers_mongo
download_question_file_task >> import_questions_mongo

import_answers_mongo >> spark_process
import_questions_mongo >> spark_process

spark_process >> import_output_mongo >> end
