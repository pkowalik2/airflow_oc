from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import requests

def head():
    r = requests.head("https://www.google.com")
    return r.headers



dag = DAG('dag1', description='dag1',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2017, 3, 20), catchup=False,
        )

task_one = PythonOperator(
    task_id="task_one", python_callable=print_hello, dag=dag
)

task_one
