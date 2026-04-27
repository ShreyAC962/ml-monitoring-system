# Real-Time ML Monitoring & Auto-Retraining System

This project is a production-style Machine Learning monitoring system that:

- Streams real-time data using Kafka
- Detects data drift in live traffic
- Monitors model performance using Prometheus
- Automatically triggers:
  - Circuit Breaker
  - Model Rollback (Golden Model)
  - Auto Retraining Pipeline
- Tracks models using MLflow
- Can be deployed using Terraform on cloud

---

# Architecture Overview

Kafka → Model Inference → Drift Detection → Prometheus Monitoring → Circuit Breaker → (Rollback OR Retrain)

---

# Tech Stack

- Python
- Kafka
- MLflow
- Prometheus
- Scikit-learn
- Terraform

---

# Installation

## 1. Clone the project

```bash
git clone https://github.com/your-username/ml-monitoring-system.git
cd ml-monitoring-system
```

## Create virtual environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```


## Install dependencies
```
pip install -r requirements.txt
```

## System Requirements

Make sure you have installed:

Kafka
- Apache Kafka running locally (port 9092)
- Zookeeper running
MLflow
```mlflow ui```
Runs on: http://localhost:5000

Prometheus
```prometheus --config.file=monitoring/prometheus.yml```
Runs on: http://localhost:9090


## Run the Project
Step 1: Start Kafka
```zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

- Create topic:
```kafka-topics.sh --create --topic ml-stream --bootstrap-server localhost:9092
```

Step 2: Train initial model
```python model/train.py```
Creates initial “Golden Model”

Step 3: Start Kafka Producer (streaming data)
```python kafka/producer.py```

Step 4: Start Prometheus metrics server
```python monitoring/metrics.py```

Step 5: Run main system (core engine)
```python app.py```

## What happens when you run it
1. Kafka streams real-time data
2. Model predicts output
3. System checks:
Data drift
Model accuracy
4. If problem detected:
Circuit breaker activates
Old model restored (rollback)
New model retraining starts automatically


## Key Features
- Drift Detection
Detects changes in data distribution using statistical comparison.

- Circuit Breaker
Stops bad models from serving predictions.

- Auto Retraining
Retrains model automatically when performance drops.

- Golden Model System
Only best-performing model is deployed.

- Monitoring
Prometheus tracks:
        Accuracy
        Drift score

## FINAL FLOW (SIMPLE)
        Kafka → Data Stream
                ↓
        Model Prediction
                ↓
        Drift Detection
                ↓
        Circuit Breaker
        ↓         ↓
        Rollback   Retrain

## Testing Flow
You can test system behavior:

- Force drift:
        Modify producer values
        Or reduce accuracy threshold
- Expected output:
        Circuit breaker triggers
        Model rollback happens
        Retraining starts automatically