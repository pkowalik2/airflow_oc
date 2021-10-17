from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import requests

def head():

    try:        
        r = requests.head("https://www.google.com")
        print(r.status_code)
        print(r.headers)
    except Exception as e:
        print(e)
    
    return ''



dag = DAG('dag1', description='dag1',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2017, 3, 20), catchup=False,
        )

task_one = PythonOperator(
    task_id="task_one", python_callable=head, dag=dag
)

task_one
