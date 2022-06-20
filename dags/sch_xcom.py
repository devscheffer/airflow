from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from random import uniform
from datetime import datetime

default_args = {"start_date": datetime(2020, 1, 1)}

def _spark_subit_update(spark_submit_new):
    spark_submit_default={}
    spark_param=spark_submit_default.update(spark_submit_new)
    return spark_param

def _choose_spark(ti):
    spark_option_size = [
        {"max_size": 100, "spark_param": {}},
        {"max_size": 10, "spark_param": {}},
        {"max_size": 1, "spark_param": {}},
    ]
    spark_option_size_v1=sorted(spark_option_size, key=lambda x: x['max_size'], reverse=False)
    database_size = ti.xcom_pull(key='database_size',task_ids=["database_size"])[0]
    for i in spark_option_size_v1:
        if database_size < i.get('max_size'):
            spark_submit=_spark_subit_update(i)
            ti.xcom_push(key='spark_submit',value=spark_submit)
def _size(ti):
    ti.xcom_push(key='database_size',value=11)

with DAG(
    "xcom_dag", schedule_interval="@daily", default_args=default_args, catchup=False
) as dag:
    hadoop_cmd = BashOperator(task_id="hadoop_cmd", bash_command="sleep 3")
    database_size = PythonOperator(task_id="database_size",python_callable=_size,provide_context=True)
    spark_size = PythonOperator(
        task_id="Choose_spark_size", python_callable=_choose_spark, provide_context=True
    )

hadoop_cmd >> database_size>>spark_size
