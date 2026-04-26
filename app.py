from kafka import KafkaConsumer # To read streaming data from Kafka topic
import json
from model.predict import predict
from model.drift import detect_drift
from services.circuit_breaker import check_model_health
from services.rollback import rollback_to_best
from services.retrain import retrain_model
from monitoring.metrics import update_metrics, start_metrics_server # Import functions to update metrics and start Prometheus server


old_data = [0.5,0.6,0.55] # Baseline data used to compare drift

def main():

    start_metrics_server() 

    consumer = KafkaConsumer(
        'ml-stream', # Subscribe to Kafka topic 'ml-stream'
        bootstrap_servers='localhost:9092', # Kafka server address
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # incomming bytes -> JSON dictionary
    )

    for message in consumer:
        data = message.value

        prediction = predict(data)
        new_data =[data["feature1"], data["feature2"]]

        drift = detect_drift(old_data, new_data)

        accuracy = 0.7 # Simulated accuracy value

        update_metrics(accuracy, drift)

        if check_model_health(accuracy, drift):
            print("Circuit Breaker Triggered")
            rollback_to_best()
            retrain_model()

        print("Prediction", predict)

if __name__ == "__main__":
    main()  
