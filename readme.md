# Airflow
## install using docker
https://www.youtube.com/watch?v=aTaytcxy2Ck

```
curl -X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"
```
## Use airlow CLI

container id = be4091be1261
```
docker exec be4091be1261 <cmd>
```
example
```
docker exec be4091be1261 airflow -h
```
## Create user
```
docker exec be4091be1261 airflow users create -u scheffer -p scheffer -f Gerson -l Scheffer -r Admin -e scheffer@airflow.com
```
## CMD

airflow db init

--
test task
```
airflow tasks test <dag id> <task id> <execution date in the past yyyy-MM-dd>
```
