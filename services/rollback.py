import mlflow

def rollback_to_best():
    # Create an MLflow client to interact with experiment runs
    client = mlflow.tracking.MlflowClient()

    # Search all runs, sort by accuracy(highest first), pick the best run
    latest = client.search_runs(order_by=["metrics.accuracy DESC"])[0]

    # Print the run ID of the best model - used for rollback
    print("Rolling back to: ", latest.info.run_id)
