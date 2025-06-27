from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'shivanshu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')  # ✅ Corrected "keys" to "key"
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    print(f"Hello world! My name is {first_name} {last_name}, and I am {age} years old!")  # ✅ Fixed f-string

def get_name(ti):
    ti.xcom_push(key='first_name', value='shiv')
    ti.xcom_push(key='last_name', value='srivastava')

with DAG(
    default_args=default_args,
    dag_id='our_first_dag_v_07',
    description='This is our first dag using python operator',
    start_date=datetime(2024, 6, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={'age': 20}
    )

    task2 >> task1
