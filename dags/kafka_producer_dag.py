from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaProducer
import json

def send_message():
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    message = {"type": "greet", "content": "Triggering agent workflow"}
    producer.send("ai_agent_input", message)
    producer.flush()
    print(f"✅ Sent message: {message}")

with DAG(
    dag_id="kafka_producer_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    send_task = PythonOperator(
        task_id="send_kafka_message",
        python_callable=send_message
    )
