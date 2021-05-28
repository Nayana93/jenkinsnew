from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import sqlite3
import pandas as pd
import snowflake as sn
import time

import logging

import xlsxwriter
from snowflake.connector.pandas_tools import write_pandas
import xlsxwriter
import logging


# Create your tests here.

default_args = {
    'owner': 'me',
    'start_date': datetime(2018, 9, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    'catchup_by_default': False,
}

dag = DAG(
    dag_id = 'snowflake_dag',
    default_args= default_args,
    schedule_interval =  '*/5 * * * *',
    catchup=False)

def start():
    logging.info("starttak")
    return "snowflaketask"


def snoflake():
    username = ''
    password = ''
    account = ''
    warehouse = ''
    database = ''
    ctx = sn.connector.connect(
        user=username,
        password=password,
        account=account,
        # warehouse=warehouse,
        database=database,
        schema='PUBLIC'
    )
    con = sqlite3.connect(r"db.sqlite3")
    print(con)
    df = pd.read_sql_query("SELECT * from student where CREATED_AT  = date() ", con, )
    logging.basicConfig(level=logging.DEBUG, filename='testlog.log', filemode='w')
    logging.debug("uses .02")
    logging.debug("credit used by SELECT * FROM TEST_TABLE is .02")
    df.to_excel('test.xlsx', engine='xlsxwriter', index=False)
    exc = pd.read_excel("test.xlsx")
    cs = ctx.cursor()
    write_pandas(ctx, exc, 'STUDENT')
    # print(df)
    cs.execute("SELECT current_version()")
    con.close()
    one = cs.fetchone()

    test = cs.execute(" SELECT * FROM TEST_TABLE")
    logging.debug("dfasfa %s " % test)



    cs.close()
    ctx.close()
starttask = PythonOperator(
    task_id="starttask",
    python_callable=start,
    dag=dag)
snowflaketask = PythonOperator(
    task_id="snowflaketask",
    python_callable=snoflake,
    dag=dag)
starttask >> snowflaketask