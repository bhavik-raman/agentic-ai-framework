FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir kafka-python

COPY message_router.py /app/message_router.py

CMD ["python", "/app/message_router.py"]
