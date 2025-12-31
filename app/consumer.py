import json
from kafka import KafkaConsumer

# Kafka broker address
KAFKA_BROKER = 'localhost:9092'  # Replace with your Kafka broker address

# Kafka topic
TOPIC_NAME = 'patient_vitals'

# Create Kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

if __name__ == '__main__':
    for message in consumer:
        print(f'Received message: {message.value}')
