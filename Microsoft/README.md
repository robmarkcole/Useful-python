## Microsoft
I use OneNote daily, Excel quite often for sharing data and basic analytics. Microsoft Azure is one of the 3 main choices for cloud computing. I am familiar with Azure Jupyter notebooks, but otherwise not familiar with the Azure stack. Other notable products include their business reporting tooles, e.g. [Power BI](https://powerbi.microsoft.com/en-us/report-server/)

## Azure
* Wide variety of products, viewable from your personal dashboard ('portal') -> https://portal.azure.com/ 
* [AWS to Azure services comparison](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services)

List of services in alphabetical order:

#### Azure Cache for Redis
* https://azure.microsoft.com/en-us/services/cache/
* A fully managed version of the popular open-source Redis server with a turnkey caching solution.
* https://redis.io/ -> in-memory data structure store, used as a database, cache and message broker

#### Azure Cognitive services
* https://docs.microsoft.com/en-us/azure/cognitive-services/
* Wide range of services, including vision and time series anomaly detection
* https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/overview

#### Azure container registry
* Private regsitry of docker containers
* https://azure.microsoft.com/en-us/services/container-registry/

#### Azure Cosmos DB
* https://azure.microsoft.com/en-gb/services/cosmos-db/
* NoSQL

## Custom Vision
* https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/?WT.mc_id=AI4DEV01-blog-heboelma
* Custom Vision lets you build, deploy, and improve your own image classifiers. An image classifier is an AI service that applies labels (which represent classes) to images, based on their visual characteristics.
* Article on [model training](https://towardsdatascience.com/create-a-model-with-azure-custom-vision-and-python-7bc5caed82c4) and deployment via [Docker on Jetson nano](https://medium.com/microsoftazure/running-a-gpu-enabled-azure-custom-vision-docker-container-on-a-nvidia-jetson-nano-db8747b00b4f) (flask app)


#### Azure DataBricks -> Spark
* https://azure.microsoft.com/en-gb/services/databricks/
* Integration of the [DataBricks](https://databricks.com/) platform with Azure

#### Azure Functions
* https://azure.microsoft.com/en-us/services/functions/
* Serverless functions, like AWS Lambda functions

#### Azure HDInsight
* 'Big data' solutions
* https://azure.microsoft.com/en-gb/services/hdinsight
* Easily run popular open source frameworks – including Apache Hadoop, Spark and Kafka – using Azure HDInsight, a cost-effective, enterprise-grade service for open source analytics
* Quickly spin up clusters

#### Azure IOT
* https://azure.microsoft.com/en-us/services/iot-hub/
* Used by https://www.axonize.com/

#### Azure Kubernetes Service (AKS)
* https://azure.microsoft.com/en-us/services/kubernetes-service/

#### Azure ML
* https://azure.microsoft.com/en-gb/services/machine-learning-service/
* [Data science VMs](https://azure.microsoft.com/en-gb/services/virtual-machines/data-science-virtual-machines/) -> Linux!

#### Azure Pipelines (CI)
* https://azure.microsoft.com/en-gb/services/devops/pipelines/
* Build, test, depoly
* Integrated with Github

#### Azure Jupyter Notebooks
* https://notebooks.azure.com/
* Great learning resource
* Connect from iPad with https://juno.sh/

#### Azure SQL db
* MySQL and PostgreSQL (MariaDB?)
* https://azure.microsoft.com/en-us/services/postgresql/

#### Azure SQL data & warehouse
* https://azure.microsoft.com/en-gb/services/sql-data-warehouse/
* Microsoft SQL Server

#### Azure Storage, Data Lakes & Blob storage
* https://azure.microsoft.com/en-gb/solutions/data-lake/
* Built on blob storage
* S3 equivalent for storing files up to 4.7 TB
* [Python blobgs example](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)
* [azure-storage-python](https://github.com/Azure/azure-storage-python)

#### Azure sphere
* MCU hardware integrated into their IOT platform -> https://azure.microsoft.com/en-us/services/azure-sphere/