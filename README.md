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

## ▶️ How to run the project

### Requirements
- Docker
- Docker Compose

### Start everything
``bash
docker compose up -d
Check running containers
bash
Copy code
docker compose ps
▶️ Trigger the workflow
Unpause and trigger the producer DAG:

bash

Copy code
docker exec -it airflow-webserver airflow dags unpause kafka_producer_dag
docker exec -it airflow-webserver airflow dags trigger kafka_producer_dag
📤 Expected Output
When everything is working correctly, the Agent Router logs should show something like:

text
Copy code
Agentic Router starting...
Connected to Kafka at kafka:9092
Listening on topic: ai_agent_input
Received message: {"type":"test","content":"hello from terminal"}
Sent processed message to ai_agent_output

📁 Project Structure
ai_agent_framework/
│
├── dags/                  # Airflow DAG definitions
├── src/agents/            # Agent logic
├── message_router.py      # Kafka agent router
├── Dockerfile             # Agent Router image
├── Dockerfile.airflow     # Airflow image
├── docker-compose.yml     # Service orchestration
├── requirements.txt
└── README.md

🧠 What I learned from this project

How event-driven systems work

Integrating Airflow with Kafka

Designing loosely coupled AI pipelines

Containerizing distributed systems

Debugging real-world Docker & Kafka issues

🚀 Possible Improvements

Add multiple agent types

Implement retry and failure handling

Persist agent state

Add monitoring and metrics

Dynamic DAG creation

👤 Author

Bhavik Raman
Agentic AI • Distributed Systems • Data Engineering


