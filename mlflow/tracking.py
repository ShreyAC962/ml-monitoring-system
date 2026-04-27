import mlflow

def get_best_accuracy():
    # Create an MLflow client to interact with experiment runs
    client = mlflow.tracing.MlflowClient()

    experiment = mlflow.get_experiment_by_name("ml-monitoring")


    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id], # Look only inside this experiment
        order_by=["metrics.accuracy DESC"] # Sort runs by an accuracy in descending order(best first)
    )

    if not runs:
        return 0

    # Return accuracy of the best run (top result)
    return runs[0].data.metrics["accuracy"]