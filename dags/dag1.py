from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'



resource_config = {"KubernetesExecutor": {"request_memory": "200Mi", 
                                          "limit_memory": "200Mi", 
                                          "request_cpu": "200m", 
                                          "limit_cpu": "200m"}}



dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False,
		  owner='airflow',
          executor_config = resource_config)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator