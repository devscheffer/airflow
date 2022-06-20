from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from datetime import datetime as dt

default_args = {
    "start_date": dt(2022, 4, 19),
}
with DAG(
    "user_processing",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:
    # define task/operator
    creating_table = SqliteOperator(
        task_id="creating_table",
        sqlite_conn_id="db_sqlite",
        sql="create_table.sql",
    )
