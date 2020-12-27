## Airflow
* https://airflow.apache.org
* Airflow is a platform to programmatically author, schedule and monitor workflows.
* Airflow pipelines are configuration as code (Python), allowing for dynamic pipeline generation.

### DAGs
An Airflow DAG is a collection of all the tasks you want to run, organized in a way that show their relationships and dependencies. It is defined in python files that are placed in `DAG_FOLDER` which is defined in the Airflow configuration file (`airflow.cfg`) that is in airflow_home directory.

### Operators
An operator in airflow is a dedicated task. They generally implement a single assignment and do not need to share resources with any other operators. We have to call them in correct certain order on the DAG. They generally run independently. On a DAG operators can even run on different machines. Airflow provides operators for many common tasks, including:

* BashOperator - executes a bash command
* PythonOperator - calls an arbitrary Python function
* EmailOperator - sends an email
* HTTPOperator - sends an HTTP request
* SqlOperator - executes a SQL command
* Sensor - they are a specific type of operator that will continue to work until a certain criterion is met.
* PapermillOperator - executing Jupyter Notebooks. Save the notebooks on S3

## Jupyter
* [Airflow supports integration with Papermill, which is a tool for parameterizing and executing Jupyter Notebooks](https://airflow.readthedocs.io/en/1.10.6/howto/operator/papermill.html)

## Managed 
* https://www.astronomer.io/ -> cloud and enterprise options, push custom docker images
* https://aws.amazon.com/managed-workflows-for-apache-airflow/ -> min cost about $300 a month, put DAGS on S3

## References
* [Building Data Pipeline with Airflow](https://www.linkedin.com/pulse/building-data-pipeline-airflow-mehmet-vergili/)
* [Intro to data engineering](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-i-4227c5c457d7)
* [Apache Airflow and the Future of Data Engineering: A Q&A]( https://medium.com/the-astronomer-journey/airflow-and-the-future-of-data-engineering-a-q-a-266f68d956a9)
