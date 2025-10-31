from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaConsumer
import json

def consume_messages():
    consumer = KafkaConsumer(
        'agent_responses',
        bootstrap_servers=['kafka:9092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        group_id="response_group"
    )
    for message in consumer:
        print(f"🧩 Received response: {message.value}")
        break

with DAG(
    dag_id="kafka_consumer_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    consume_task = PythonOperator(
        task_id="consume_kafka_message",
        python_callable=consume_messages
    )
