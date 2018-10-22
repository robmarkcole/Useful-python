## Airflow
* [Building Data Pipeline with Airflow](https://www.linkedin.com/pulse/building-data-pipeline-airflow-mehmet-vergili/)
* [Intro to data engineering](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-i-4227c5c457d7)

## DAG
An Airflow DAG is a collection of all the tasks you want to run, organized in a way that show their relationships and dependencies. It is defined in python files that are placed in `DAG_FOLDER` which is defined in the Airflow configuration file (`airflow.cfg`) that is in airflow_home directory.

## Operators
An operator in airflow is a dedicated task. They generally implement a single assignment and do not need to share resources with any other operators. We have to call them in correct certain order on the DAG. They generally run independently. On a DAG operators can even run on different machines. Airflow provides operators for many common tasks, including:

* BashOperator - executes a bash command
* PythonOperator - calls an arbitrary Python function
* EmailOperator - sends an email
* HTTPOperator - sends an HTTP request
* SqlOperator - executes a SQL command
* Sensor - they are a specific type of operator that will continue to work until a certain criterion is met.
