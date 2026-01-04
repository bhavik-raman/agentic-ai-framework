# Agentic AI Framework  
### Event-Driven AI Orchestration using Airflow & Kafka

This project demonstrates how an **agent-based AI workflow** can be built using
Apache Airflow for orchestration and Apache Kafka for event-driven communication.

The goal of the project is to show how tasks can be routed asynchronously through
an **Agent Router**, instead of being tightly coupled inside a single workflow.

---

## 🔍 What this project does

- Airflow triggers a workflow
- A message is published to Kafka
- An Agent Router listens to Kafka
- The agent processes the message
- The result is published back to Kafka
- Airflow consumes the processed output

This pattern is useful for building **scalable, decoupled AI systems**.

---

## 🧱 Architecture Flow

Airflow DAG
↓
Kafka (ai_agent_input)
↓
Agent Router
↓
Kafka (ai_agent_output)
↓
Airflow Consumer DAG

Each component runs independently using Docker.

---

## 🧩 Components Explained

### Apache Airflow
- Manages and triggers workflows
- Sends messages to Kafka
- Can react to processed results

### Apache Kafka
- Acts as the communication backbone
- Enables asynchronous processing
- Topics used:
  - `ai_agent_input`
  - `ai_agent_output`

### Agent Router
- A Python service running in its own container
- Uses KafkaConsumer and KafkaProducer
- Listens, processes, and forwards messages

---

## 🛠️ Tech Stack

- Python 3.12  
- Apache Airflow 2.9.3  
- Apache Kafka (Confluent)  
- PostgreSQL  
- Redis  
- Docker & Docker Compose  

---

Requirements

Before running the project, ensure you have:

Docker

Docker Compose

Running the Project
Start all services

From the project root:

docker compose up -d


This will start:

PostgreSQL

Redis

Zookeeper

Kafka

Airflow (Webserver + Scheduler)

Agent Router

Verify running containers
docker compose ps


All services should show Up.

Triggering the Workflow
Unpause the producer DAG
docker exec -it airflow-webserver airflow dags unpause kafka_producer_dag

Trigger the DAG manually
docker exec -it airflow-webserver airflow dags trigger kafka_producer_dag


This sends a message from Airflow to Kafka.

Expected Output

Check the Agent Router logs:

docker logs -f agent-router


You should see output similar to:

Agentic Router starting...
Connected to Kafka at kafka:9092
Listening on topic: ai_agent_input

Received message:
{"type":"test","content":"hello from terminal"}

Sent processed message to ai_agent_output

What This Confirms

Airflow successfully produced a Kafka message

The Agent Router consumed the message

The message was processed and forwarded correctly

Project Structure
ai_agent_framework/
│
├── dags/                 # Airflow DAG definitions
├── src/agents/           # Agent logic
├── message_router.py     # Kafka agent router
├── Dockerfile            # Agent Router image
├── Dockerfile.airflow    # Airflow image
├── docker-compose.yml    # Service orchestration
├── requirements.txt
└── README.md

Key Learnings

Event-driven system design

Integrating Apache Airflow with Kafka

Building loosely-coupled agent pipelines

Containerizing distributed systems

Debugging real-world Docker and Kafka issues

Possible Improvements

Support multiple agent types

Add retry and failure handling

Persist agent state

Add monitoring and metrics


👤 Author

Bhavik Raman
Agentic AI • Distributed Systems • Data Engineering


