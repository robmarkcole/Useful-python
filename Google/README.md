## Google Cloud Products (GCP)
* https://cloud.google.com/products/

GCP products in alphabetical order:

## AI Notebooks
* https://cloud.google.com/ai-platform-notebooks/
* An enterprise notebook service to get your projects up and running in minutes
* `$0.176` hourly CPU only, `$0.452 hourly` with GPU (1 NVIDIA Tesla K80)
* Can create instance from [custom docker container](https://cloud.google.com/ai-platform/notebooks/docs/custom-container?_ga=2.51808105.-1104585797.1574315998)
* Tensorflow 2 is supported. Example notebooks include Geronds [tf2_course](https://github.com/ageron/tf2_course)
* Notebooks is integrated with BigQuery, Cloud Dataproc, and Cloud Dataflow, making it easy to go from data ingestion to preprocessing and exploration, and eventually model training and deployment.
* There are no minimum fees or up-front commitments. There’s no charge for using Notebooks. You pay only for the cloud resources you use with the Notebooks instance
* Git jupyterlab integration is installed
* Alternatively consider Colab pro -> https://colab.research.google.com/signup

## AI VM
* Used by the Notebooks
* https://cloud.google.com/deep-learning-vm/
* The AI Platform Deep Learning VM Images are a set of Debian 9-based Compute Engine virtual machine images optimized for data science and machine learning tasks. 
* The VM images deliver a seamless notebook experience with integrated support for JupyterLab. [Connecting to Jupyter Lab](https://cloud.google.com/deep-learning-vm/docs/jupyter)

## BigQuery
* https://cloud.google.com/bigquery/
* BigQuery runs blazing-fast SQL queries on gigabytes to petabytes of data and makes it easy to join public or commercial datasets with your data
* [Getting Started With SQL and BigQuery on Kaggle](https://www.kaggle.com/dansbecker/getting-started-with-sql-and-bigquery)
* [Public datasets](https://www.reddit.com/r/bigquery/wiki/datasets)
* Export via pandas with [pandas.read_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html) that has a dependency on [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)

## BigTable
* https://cloud.google.com/bigtable/
* A petabyte-scale, fully managed NoSQL database service for large analytical and operational workloads.
* Integrates with big data tools like Hadoop & HBase

## Compute Engine
* https://cloud.google.com/compute/
* Googles alternative to EC2
* VMs -> Run your choice of OS, including Debian, CentOS, CoreOS, SUSE, Ubuntu, Red Hat Enterprise Linux, FreeBSD, or Windows Server 2008 R2, 2012 R2, and 2016.

## Composer
* https://cloud.google.com/composer/
* Managed Airflow
* Billed by CPU hours

## Data Fusion
* https://cloud.google.com/data-fusion/
* code-free development of ETL pipelines

## Data Prep
* UI for exploring and cleaning data

## Data Studio
* https://datastudio.google.com/overview
* Dasboarding & reporting
* Google have purchased Looker, perhaps this will be replacing data studio..?

## Functions
* https://cloud.google.com/functions/
* Lambda equivalent

## IOT core
* https://cloud.google.com/iot-core/
* Data ingestion, device management etc

## Storage
* https://cloud.google.com/storage/
* S3 equivalent object storage

## SQL
* [Hosted postgres](https://cloud.google.com/sql/)
* https://github.com/robmarkcole/HASS-Google-Cloud-SQL
* [Pricing](https://cloud.google.com/sql/pricing#pg-pricing) - storage per GB/month and egress, ingress is free

## Pub/Sub
* https://cloud.google.com/pubsub/
* Streaming event data
* First 10 GB per month is free
* Integrated into [Home Assistant](https://www.home-assistant.io/components/google_pubsub/)

## Python API
* https://github.com/googleapis/google-cloud-python
* [Asyncio Google Cloud Client Library for Python](https://github.com/talkiq/gcloud-aio)

## Certification
* https://cloud.google.com/certification/data-engineer