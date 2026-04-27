from kafka import KafkaConsumer  
# Import KafkaConsumer to read streaming data from Kafka topic

import json  
# Import JSON module to decode incoming Kafka messages

from collections import deque  
# Import deque (double-ended queue) for efficient sliding window storage

from model.predict import predict  
# Import ML model prediction function

from model.drift import detect_drift  
# Import drift detection function

from services.circuit_breaker import check_model_health  
# Import function to check model health (accuracy + drift)

from services.rollback import rollback_to_best  
# Import function to rollback to last good model

from services.retrain import retrain_model  
# Import function to retrain model when drift is detected

from monitoring.metrics import update_metrics, start_metrics_server  
# Import metrics functions for Prometheus monitoring


# =========================
# 🔹 Dynamic data buffers
# =========================

baseline_window = deque(maxlen=50)  
# Stores stable historical data (reference distribution)

stream_window = deque(maxlen=50)  
# Stores latest incoming streaming data


def main():

    print("Starting ML Monitoring System...")  
    # Print system start message

    start_metrics_server()  
    # Start Prometheus metrics server (exposes metrics endpoint)

    consumer = KafkaConsumer(
        'ml-stream',  
        # Subscribe to Kafka topic "ml-stream"

        bootstrap_servers='localhost:9092',  
        # Kafka broker address

        value_deserializer=lambda m: json.loads(m.decode('utf-8'))  
        # Convert Kafka bytes message into Python dictionary
    )

    for message in consumer:
        # Continuously listen to streaming data

        data = message.value  
        # Extract actual data from Kafka message

        # =========================
        # 1. Prediction
        # =========================
        prediction = predict(data)  
        # Run ML model to get prediction

        # =========================
        # 2. Update streaming buffer
        # =========================
        stream_window.append(data["feature1"])  
        # Add feature1 to streaming buffer

        stream_window.append(data["feature2"])  
        # Add feature2 to streaming buffer

        # initialize baseline if empty
        if len(baseline_window) < 10:
            # If baseline is not yet enough, initialize it

            baseline_window.append(data["feature1"])  
            # Add feature1 to baseline

            baseline_window.append(data["feature2"])  
            # Add feature2 to baseline

            continue  
            # Skip rest until baseline is ready

        # =========================
        # 3. Drift detection
        # =========================
        drift = detect_drift(
            list(baseline_window),  
            # Convert baseline deque to list

            list(stream_window)  
            # Convert streaming deque to list
        )

        # =========================
        # 4. Simulated accuracy
        # =========================
        accuracy = 0.7  
        # Placeholder accuracy (in real system: computed from eval pipeline)

        # =========================
        # 5. Update monitoring metrics
        # =========================
        update_metrics(accuracy, drift)  
        # Send accuracy and drift to Prometheus

        # =========================
        # 6. Circuit breaker logic
        # =========================
        if check_model_health(accuracy, drift):
            # If model is unhealthy (low accuracy or drift detected)

            print("CIRCUIT BREAKER TRIGGERED")  
            # Alert system is taking recovery action

            rollback_to_best()  
            # Restore last best model

            retrain_model("drift")  
            # Trigger retraining due to drift

            baseline_window.clear()  
            # Reset baseline after retraining

        # =========================
        # 7. Logging
        # =========================
        print("Prediction:", prediction)  
        # Print model prediction result

        print("Drift detected:", drift)  
        # Print whether drift is detected


if __name__ == "__main__":
    # Entry point of program

    main()  
    # Start the ML monitoring pipeline