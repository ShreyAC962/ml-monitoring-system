from kafka import KafkaProducer
import json, time, random

# Creating a Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', # Conecting to Kafka broker running locally on port 9092
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Covert python dict -> JSON string -> bytes(Kafka needs bytes)  
)

# Infinte loop to continuously send data
while True:
    data = {
        "feature1" : random.random(), # Generate a random float between 0 and 1
        "feature2" : random.random(), # Generate another random float
        "label" : random.randint(0,1) # Generate a random label (0 or 1)
    }

    producer.send("ml-stream", data) # Send this data to Kafka topic named "ml-stream"

    time.sleep(1) # Wait for one second before sending next message