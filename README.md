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

▶️ How to Run the Project
🔧 Requirements

Make sure the following are installed on your system:

Docker

Docker Compose

▶️ Start all services

Run the following command from the project root:

docker compose up -d


This will start:

PostgreSQL

Redis

Zookeeper

Kafka

Airflow (webserver + scheduler)

Agent Router

🔍 Check running containers

To verify that all services are running:

docker compose ps


All containers should show Up status.

▶️ Trigger the Workflow
1️⃣ Unpause the producer DAG
docker exec -it airflow-webserver airflow dags unpause kafka_producer_dag

2️⃣ Trigger the DAG manually
docker exec -it airflow-webserver airflow dags trigger kafka_producer_dag


This sends a message from Airflow to Kafka.

📤 Expected Output

When everything is working correctly, check the Agent Router logs:

docker logs -f agent-router


You should see output similar to this:

Agentic Router starting...
Connected to Kafka at kafka:9092
Listening on topic: ai_agent_input
Received message: {"type":"test","content":"hello from terminal"}
Sent processed message to ai_agent_output


This confirms that:

Airflow successfully produced a Kafka message

The Agent Router consumed it

The message was processed and forwarded

✅ Result

The full pipeline works end-to-end:

Airflow → Kafka → Agent Router → Kafka → Airflow
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


