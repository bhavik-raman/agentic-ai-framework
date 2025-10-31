import time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import NoBrokersAvailable, KafkaError

BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC_IN = "ai_agent_input"
TOPIC_OUT = "ai_agent_output"

print("🧠 Agentic Router starting...")

# Wait for Kafka to be ready
for attempt in range(1, 11):
    try:
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
        consumer = KafkaConsumer(
            TOPIC_IN,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="agentic-router",
        )
        print(f"✅ Connected to Kafka on {BOOTSTRAP_SERVERS}")
        break
    except NoBrokersAvailable:
        print(f"⚠️ Kafka not ready (attempt {attempt}/10)... waiting 5s")
        time.sleep(5)
else:
    print("❌ Could not connect to Kafka after multiple attempts. Exiting.")
    exit(1)

print(f"🎧 Listening for messages on topic: {TOPIC_IN}")

# Main message loop
while True:
    try:
        for msg in consumer:
            text = msg.value.decode("utf-8")
            print(f"📥 Received: {text}")

            # Simulate processing
            result = f"Processed message: {text}"
            producer.send(TOPIC_OUT, result.encode("utf-8"))
            producer.flush()
            print(f"📤 Sent: {result}")

    except KafkaError as e:
        print(f"❌ Kafka error: {e}")
        time.sleep(5)
