## Real-Time ML Monitoring & Auto-Retraining System

Built a system that:
Watches ML models in real time
Detects data drift + performance drop
Automatically:
Rolls back to a safe model (“Golden Model”)
Retrains a new model
No human needed


## Tools
MLflow - Track models, versions, metrics
Prometheus - Collect metrics (accuracy, drift, latency)
Apache Kafka - Real-time data streaming
Vertex AI - Train & deploy models
Python - Core logic
Terraform - Automate cloud setup

## High-Level Architecture
```
[Kafka Stream] → [Model Service] → [Metrics Collector]
                                      ↓
                             [Prometheus]
                                      ↓
                         [Drift Detection Service]
                                      ↓
                            ┌───────────────┬
                            ↓               ↓
                    Rollback Model     Trigger Retraining
                            ↓               ↓
                        MLflow         Vertex AI Training
```

## Project Structure
```
ml-monitoring-system/
│
├── data/
│   └── sample_stream.json
│
├── kafka/
│   └── producer.py
│
├── model/
│   ├── train.py
│   ├── predict.py
│   └── drift.py
│
├── monitoring/
│   ├── metrics.py
│   └── prometheus.yml
│
├── services/
│   ├── circuit_breaker.py
│   ├── retrain.py
│   └── rollback.py
│
├── mlflow/
│   └── tracking.py
│
├── terraform/
│   └── main.tf
│
├── app.py
├── requirements.txt
└── README.md
```

## Install System Setup
```
pip install mlflow prometheus_client kafka-python scikit-learn pandas numpy fastapi uvicorn
```