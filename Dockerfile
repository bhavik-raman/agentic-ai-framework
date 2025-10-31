FROM apache/airflow:2.9.3

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch to airflow user for Python package installation
USER airflow

# Install Kafka client under airflow user
RUN pip install --no-cache-dir kafka-python

WORKDIR /opt/airflow

# Copy project files
COPY ./src /opt/airflow/src
COPY ./dags /opt/airflow/dags

# Default command
CMD ["python", "/opt/airflow/src/agents/message_router.py"]
