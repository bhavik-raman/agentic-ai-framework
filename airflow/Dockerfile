FROM apache/airflow:2.9.3

USER airflow

# Install kafka-python properly as the airflow user
RUN pip install --no-cache-dir kafka-python

USER root
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

USER airflow
