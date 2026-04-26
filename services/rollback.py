import mlflow

def rollback_to_best():
    # Create an MLflow client to interact with experiment runs
    client = mlflow.tracking.MlflowClient()

    experiment = mlflow.get_experiment_by_name("ml-monitoring")

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id], # Look only inside this experiment
        order_by=["metrics.accuracy DESC"] # Sort runs by an accuracy in descending order(best first)
    )

    if not runs:
        print("No runs found")
        return

    best_run = runs[0] # Select the top run - highest accuracy model

    print("Rolling back to run:", best_run.info.run_id) # Print the ID of the best model run(used for rollback)
