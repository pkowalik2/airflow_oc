from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'


dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False,
        )

one_task = PythonOperator(
    task_id="one_task", python_callable=hello_world, dag=dag,
    executor_config={"KubernetesExecutor": {"image": "apache/airflow:latest"}}
)

one_task
