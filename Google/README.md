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
* BigQuery runs blazing-fast SQL queries on gigabytes to petabytes of data and makes it easy to join public or commercial datasets with your data
* [Getting Started With SQL and BigQuery on Kaggle](https://www.kaggle.com/dansbecker/getting-started-with-sql-and-bigquery)
* [Public datasets](https://www.reddit.com/r/bigquery/wiki/datasets)
* Export via pandas with [pandas.read_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html) that has a dependency on [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)
* [How to do time series forecasting in BigQuery Using ARIMA](https://towardsdatascience.com/how-to-do-time-series-forecasting-in-bigquery-af9eb6be8159) and [notebook](https://github.com/GoogleCloudPlatform/bigquery-oreilly-book/blob/master/blogs/bqml_arima/bqml_arima.ipynb)
* Book [BigQuery: The Definitive Guide](https://github.com/GoogleCloudPlatform/bigquery-oreilly-book)

## BigTable
* A petabyte-scale, fully managed NoSQL database service for large analytical and operational workloads.
* Integrates with big data tools like Hadoop & HBase

## Compute Engine
* Googles alternative to EC2
* VMs -> Run your choice of OS, including Debian, CentOS, CoreOS, SUSE, Ubuntu, Red Hat Enterprise Linux, FreeBSD, or Windows Server 2008 R2, 2012 R2, and 2016.

## Composer
* Managed Airflow
* Billed by CPU hours

## Dataflow
* stream and batch data processing. 
* Dataflow is a fully-managed service on Google Cloud that can be used for data processing. You can write your Dataflow code and then use Airflow to schedule and monitor Dataflow job. Airflow also allows you to retry your job if it fails (number of retries is configurable). You can also configure in Airflow if you want to send alerts on Slack or email, if your Dataflow pipeline fails.
* You can use the Dataflow SQL streaming extensions to aggregate data from continuously updating Dataflow sources like Pub/Sub into BigQuery

## Data Fusion
* code-free development of ETL pipelines

## Data Prep
* UI for exploring and cleaning data

## Data Studio
* https://datastudio.google.com/overview
* Dasboarding & reporting
* Google have purchased Looker, perhaps this will be replacing data studio..?

## Functions
* Lambda equivalent

## IOT core
* Data ingestion, device management etc

## Storage
* S3 equivalent object storage

## SQL
* https://github.com/robmarkcole/HASS-Google-Cloud-SQL
* [Pricing](https://cloud.google.com/sql/pricing#pg-pricing) - storage per GB/month and egress, ingress is free

## Pub/Sub
* Streaming event data
* First 10 GB per month is free
* Integrated into [Home Assistant](https://www.home-assistant.io/components/google_pubsub/)

## Python API
* https://github.com/googleapis/google-cloud-python
* [Asyncio Google Cloud Client Library for Python](https://github.com/talkiq/gcloud-aio)

## Certification
* https://cloud.google.com/certification/data-engineer

## Training - qwiklabs
* https://www.qwiklabs.com -> online labs including all required resources in a sandbox ([watch](https://google.qwiklabs.com/focuses/605?locale=en&parent=catalog&qlcampaign=yt18-gsp088-74577))
* Get temporary access to the Google Cloud Console (you are given a username, password and project for each lab)
* Over 200 labs from beginner to advanced levels.
* It is necessary to purchase credits to run the labs

Courses to-do
* [Baseline: Data, ML, AI](https://google.qwiklabs.com/quests/34)
* [Data Engineering](https://google.qwiklabs.com/quests/25?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=5195293)
* [Scientific Data Processing](https://google.qwiklabs.com/quests/28?catalog_rank=%7B%22rank%22%3A7%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=5195293) -> tasks like earthquake data analysis and satellite image aggregation
* [Data Science on Google Cloud](https://google.qwiklabs.com/quests/43?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=5195293)

## Google search engine
* https://varvy.com/googlebot.html -> googles web crawler