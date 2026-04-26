from prometheus_client import start_http_server, Gauge

accuracy_gauge = Gauge('model_accuracy', 'Model Accuracy')

drift_gauge = Gauge('data_drift', 'Data Drift')

def update_metrics(acc, drift):
  accuracy_gauge.set(acc)
  drift_gauge.set(drift)

# Prometheus can scrape metrics from: http://localhost:8000
# To start a web server on port 8000 to expose metrics
start_http_server(8000)