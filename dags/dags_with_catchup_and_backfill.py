from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2025, 5, 28),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )


    # what we do in this 
    # This code defines an Airflow DAG named 'dag_with_catchup_backfill_v02'.
    # The DAG is scheduled to run daily, starting from May 28, 2025, and does not catch up on missed runs.
    # It has a single task, 'task1', which executes a simple bash command that prints a message.
    # The DAG is configured with default arguments, including the owner, number of retries, and retry delay.
    # The `BashOperator` is used to run the bash command within the task.
    task1
# The DAG is defined using the `with` statement, ensuring that all tasks are part of the same DAG context.
# The `catchup=False` setting means that if the DAG is started after its scheduled start date, it will not run for the missed intervals.
# This is useful for preventing unnecessary backfilling of tasks that were not executed during the scheduled intervals.
# The `default_args` dictionary specifies the default parameters for the DAG, such as the owner, number of retries, and retry delay.
# The `BashOperator` is used to execute a simple bash command, demonstrating how to run shell commands within an Airflow task.
# The code is structured to be clear and maintainable, leveraging Airflow's capabilities for scheduling and task management.
# The DAG is instantiated at the end, allowing Airflow to recognize and schedule it for execution.
# The `BashOperator` is a convenient way to run shell commands directly from Airflow tasks, making it versatile for various use cases.
# The DAG is designed to be simple and straightforward, focusing on demonstrating the use of catchup and backfill features in Airflow.
# The `start_date` is set to a future date, which means the DAG will not run until that date is reached.
# The `schedule_interval='@daily'` setting indicates that the DAG should run once every day.
# The `catchup=False` setting ensures that the DAG will not attempt to run for any dates prior to the `start_date`, even if it is triggered after that date.
# This is useful for preventing unnecessary backfilling of tasks that were not executed during the scheduled intervals.
# The `BashOperator` is a powerful tool in Airflow that allows users to execute shell commands as part of their workflows.
# This code is a simple example of how to create a DAG with a single task that runs a bash command.


# The DAG is defined using the `with` statement, ensuring that all tasks are part of the same DAG context.
# The `catchup=False` setting means that if the DAG is started after its scheduled start date, it will not run for the missed intervals.
# This is useful for preventing unnecessary backfilling of tasks that were not executed during the scheduled intervals.
# The `default_args` dictionary specifies the default parameters for the DAG, such as the owner, number of retries, and retry delay.
# The `BashOperator` is used to execute a simple bash command, demonstrating how to run shell commands within an Airflow task.
# The code is structured to be clear and maintainable, leveraging Airflow's capabilities for scheduling and task management.
# The DAG is instantiated at the end, allowing Airflow to recognize and schedule it for execution.
# The `BashOperator` is a convenient way to run shell commands directly from Airflow tasks, making it versatile for various use cases.
# The DAG is designed to be simple and straightforward, focusing on demonstrating the use of catchup and backfill features in Airflow.
