import json
import time
import random
from kafka import KafkaProducer

# Kafka broker address
KAFKA_BROKER = 'localhost:9092'  # Replace with your Kafka broker address

# Kafka topic
TOPIC_NAME = 'patient_vitals'

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def generate_vitals():
    patient_id = random.randint(1, 100)
    heart_rate = random.randint(60, 100)
    blood_pressure = f'{random.randint(110, 140)}/{random.randint(70, 90)}'
    temperature = round(random.uniform(36.5, 37.5), 1)
    return {
        'patient_id': patient_id,
        'heart_rate': heart_rate,
        'blood_pressure': blood_pressure,
        'temperature': temperature,
        'timestamp': time.time()
    }


if __name__ == '__main__':
    while True:
        vitals = generate_vitals()
        print(f'Sending vitals: {vitals}')
        producer.send(TOPIC_NAME, vitals)
        time.sleep(1)
