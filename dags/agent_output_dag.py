from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaConsumer
import json

BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC_OUT = "ai_agent_output"

def process_kafka_messages():
    consumer = KafkaConsumer(
        TOPIC_OUT,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="airflow-consumer"
    )

    for msg in consumer:
        text = msg.value.decode("utf-8")
        print(f"📩 [Airflow DAG] Received from Agent: {text}")
        # Here you can trigger additional Airflow tasks or workflows
        break  # process one message at a time

with DAG(
    dag_id="agent_output_listener",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:
    listen_task = PythonOperator(
        task_id="listen_agent_output",
        python_callable=process_kafka_messages,
    )
