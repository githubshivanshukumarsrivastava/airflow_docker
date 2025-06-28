from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'shiv',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_s02",
    start_date=datetime(2025, 5, 1),
    #schedule_interval='@daily'# or '0 0 * * *'  # Cron expression for daily at midnight
    schedule_interval='0 0 * * *',  # Cron expression for daily at midnight
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1