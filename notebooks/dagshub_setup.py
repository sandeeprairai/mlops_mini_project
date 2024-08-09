import mlflow
import dagshub
dagshub.init(repo_owner='sandeeprairai', repo_name='mlops_mini_project', mlflow=True)


mlflow.set_tracking_uri('https://dagshub.com/sandeeprairai/mlops_mini_project.mlflow')

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)