## Kubeflow
* Kubeflow is a ML platform running on kubernetes using best-in-class tools
* KubeFlow is a modern, end-to-end pipeline orchestration framework that embraces the latest AI best practices including hyper-parameter tuning, distributed model training, and model tracking.
* https://www.kubeflow.org/
* Kubeflow Pipelines are a new component of Kubeflow that can help you compose, deploy, and manage end-to-end (optionally hybrid) machine learning workflows. -> https://cloud.google.com/blog/products/ai-machine-learning/getting-started-kubeflow-pipelines

## Example ML worflow
KubeFlow is a modern, end-to-end pipeline orchestration framework that embraces the latest AI best practices including hyper-parameter tuning, distributed model training, and model tracking.

XGBoost results on the pipelines UI

Airflow is the most-widely used pipeline orchestration framework in machine learning and data engineering.

MLflow is a lightweight experiment-tracking system recently open-sourced by Databricks, the creators of Apache Spark. MLflow supports Python, Java/Scala, and R - and offers native support for TensorFlow, Keras, and Scikit-Learn.

1. Create a Kubernetes cluster
2. Install KubeFlow, Airflow, TFX, and Jupyter
3. Setup ML Training Pipelines with KubeFlow and Airflow
4. Transform Data with TFX Transform
5. Validate Training Data with TFX Data Validation
6. Train Models with Jupyter, Keras/TensorFlow 2.0, PyTorch, XGBoost, and KubeFlow
7. Run a Notebook Directly on Kubernetes Cluster with KubeFlow
8. Analyze Models using TFX Model Analysis and Jupyter
9. Perform Hyper-Parameter Tuning with KubeFlow
10. Select the Best Model using KubeFlow Experiment Tracking
11. Run Multiple Experiments with MLflow Experiment Tracking
12. Reproduce Model Training with TFX Metadata Store
13. Deploy the Model to Production with TensorFlow Serving and Istio
14. Save and Download your Workspace