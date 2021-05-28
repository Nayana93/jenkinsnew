from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.utils.dates import days_ago

default_args = {'owner': 'airflow'}

dag = DAG(
    dag_id='example_sqlite',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(2),
    tags=['example'],
)

# [START howto_operator_sqlite]

# Example of creating a task that calls a common CREATE TABLE sql command.
create_table_sqlite_task = SqliteOperator(
    task_id='create_table_sqlite',
    sqlite_conn_id='sqlite_conn_id',
    sql=r"""
    CREATE TABLE table_name (
        column_1 string,
        column_2 string,
        column_3 string
    );
    """,
    dag=dag,
)

# [END howto_operator_sqlite]

# [START howto_operator_sqlite_external_file]

# Example of creating a task that calls an sql command from an external file.
external_create_table_sqlite_task = SqliteOperator(
    task_id='create_table_sqlite_external_file',
    sqlite_conn_id='sqlite_conn_id',
    sql='/scripts/create_table.sql',
    dag=dag,
)

# [END howto_operator_sqlite_external_file]

create_table_sqlite_task >> external_create_table_sqlite_task