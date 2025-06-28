from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v02', 
     default_args=default_args, 
     start_date=datetime(2021, 10, 26), 
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridman'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'],
          age=age)

greet_dag = hello_world_etl()


# what iwe are doing explain it
# This code defines an Airflow DAG using the TaskFlow API.
# The DAG is named 'dag_with_taskflow_api_v02' and is scheduled to run daily.
# It consists of three tasks:
# 1. `get_name`: Returns a dictionary with first and last names.
# 2. `get_age`: Returns a fixed age.
# 3. `greet`: Prints a greeting message using the names and age.
# The tasks are defined using the `@task` decorator, which simplifies task creation.
# The `greet` task is called with the outputs of the previous tasks.
# The DAG is instantiated at the end with `greet_dag = hello_world_etl()`.
# The `@dag` decorator is used to define the DAG, and the `@task` decorator is used to define tasks within the DAG.
# The `multiple_outputs=True` option in the `get_name` task allows it to return multiple values as a dictionary.
# The `greet` task uses f-strings for formatted output, making the code cleaner and more readable.
# The DAG is designed to run daily, starting from October 26, 2021, and has retry logic in case of failures.
# The `default_args` dictionary specifies default parameters for the DAG, such as the owner, number of retries, and retry delay.
# The code is structured to be clear and maintainable, leveraging Airflow's TaskFlow API for better readability and ease of use.

