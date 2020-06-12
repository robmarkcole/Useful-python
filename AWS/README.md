# AWS
* https://aws.amazon.com/products
* Docs -> https://docs.aws.amazon.com/index.html
* [Free tier - many services (dunamoDB & lambda) always free](https://aws.amazon.com/free)
* [How to build a SaaS for free with AWS free tier](https://hackernoon.com/how-to-build-a-saas-with-0-fed2341078c8)

## API-Gateway
* https://aws.amazon.com/api-gateway/
* Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With a few clicks in the AWS Management Console, you can create REST and WebSocket APIs that act as a “front door” for applications to access data, business logic, or functionality from your backend services, such as workloads running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, any web application, or real-time communication applications.
* [Deploy deep learning models with api-gateway and lambda](https://course.fast.ai/deployment_aws_lambda.html)

## Athena
* https://aws.amazon.com/athena
* An interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

## Aurora
* https://aws.amazon.com/rds/aurora
* MySQL and PostgreSQL-compatible relational database built for the cloud. Performance and availability of commercial-grade databases at 1/10th the cost.

## Batch
* https://aws.amazon.com/batch/
* Efficiently run hundreds of thousands of batch computing jobs on AWS
* Jobs run in docker containers on an EC2 imnstance, or on ECR

## Cloud9
* https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html
* Web IDE -> used when creating lambda functions
* Amazon bought this and it is no longer open source

## CloudFormation
* https://aws.amazon.com/cloudformation/
* AWS CloudFormation provides a common language for you to model and provision AWS and third party application resources in your cloud environment.

## Cloudwatch
* https://aws.amazon.com/cloudwatch/
* a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers
* [Plugin for grafana](https://grafana.com/grafana/plugins/cloudwatch)

## Data Pipeline
* https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html
* Similar concepts to Airflow, but AWS only
* Jobs are typically time scheduled
* Works with DynamoDB, RDS, Redshift, S3
* Example use case: Copy RDS or DynamoDB tables to S3, transform data structure, run analytics using SQL queries and load it to Redshift.

## (Data) Lake Formation
* https://aws.amazon.com/lake-formation
* a service that makes it easy to set up a secure data lake in days

## DynamoDB
* https://aws.amazon.com/dynamodb/
* NoSQL
* DynamoDB is [free for your first 25 GB](https://aws.amazon.com/free/) or [download a local Docker version](https://hub.docker.com/r/amazon/dynamodb-local)
* [Rekognition with dynamoDB backend](https://read.acloud.guru/building-an-imgur-clone-part-2-image-rekognition-and-a-dynamodb-backend-abc9af300123)
* Tables can be created from python [using boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)

## EC2
* https://aws.amazon.com/ec2/
* On demand compute
* [EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) -> automatically add or remove EC2 instances according to conditions you define

## Elastic Beanstalk
* https://aws.amazon.com/elasticbeanstalk/
* An easy-to-use service for deploying and scaling web applications and services

## Elastic Container Regsitry (ECR)
* https://docs.aws.amazon.com/ecr/index.html
* a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. 

## Elastic Load Balancing (ELB)
* https://aws.amazon.com/elasticloadbalancing/
* automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions.

## Elastic Map Reduce (EMR)
* https://aws.amazon.com/emr/
* A web service which provides a managed Hadoop framework is useful for computing large data sets.

## Firehose
* Used for ingesting streaming data
* https://aws.amazon.com/kinesis/data-firehose/
* https://towardsdatascience.com/delivering-real-time-streaming-data-to-amazon-s3-using-amazon-kinesis-data-firehose-2cda5c4d1efe

## Glue
* https://aws.amazon.com/glue/
* Transform and move AWS Cloud data into your data lake/warehouse ('big data' focus?)
* AWS Glue consists of a Data Catalog which is a central metadata repository, an ETL engine that can automatically generate Scala or Python code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries.
* [Airflow vs. AWS Glue](https://www.astronomer.io/guides/airflow-vs-aws-glue/) - TLDR Glue cannot be implemented on-premise or in any other cloud environment, requires data to be in AWS. If you need to access data from outside AWS (e.g. from an API) then Airflow can be used.
* [When should I use AWS Glue vs. AWS Data Pipeline?](https://aws.amazon.com/glue/faqs/) -> data pipeline provides greater flexibility over the execution environment, access and control over the compute resources that run your code, as well as the code itself that does data processing
* Nice article demoing use of Glue [here](https://francescopochetti.com/covid-19-end-to-end-analytics-with-aws-glue-athena-and-quicksight/)

## Kafka (MSK)
* https://aws.amazon.com/msk
* Managed Streaming for Apache Kafka

## Kinesis
* https://aws.amazon.com/kinesis/
* Easily collect, process, and analyze video and data streams in real time
* [Kinesis is modeled after Apache Kafka](https://medium.com/faun/apache-kafka-vs-apache-kinesis-57a3d585ef78)
* [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) -> [getting started](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/getting-started.html) -> **TLDR** using C++ and Gstreamer, with [Pi example here](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi.html)

## Kinesis Data Firehose
* https://aws.amazon.com/kinesis/data-firehose/
* Prepare and load real-time data streams into data stores and analytics tools
 
## Lambda
* https://aws.amazon.com/lambda/
* Functions in the cloud, can be written in python etc. 'Serverless' computing, handles scaling etc, but can be slower responses than running a dedicated server.
* [Python walkthrough](https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html) & [python official docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
* [Deploy Sklearn to Lambda](https://github.com/ryansb/sklearn-build-lambda)
* As your function development progresses, you will want to store your function code in source control. [A deployment package](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) is a ZIP archive that contains your function code and dependencies.

## Marketplace
* https://aws.amazon.com/marketplace/
* AWS Marketplace is a digital catalog that offers thousands of pre-configured software services from independent software vendors. AWS Marketplace offers a broad range of solutions ranging from operating systems to data analytics.

## Quicksight
* https://aws.amazon.com/quicksight
* Pay-per-view analytics dashboard
* Little bit alpha - some glitchy behaviour
* Data can be cached in [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html#spice) for faster queries, with 1GB available by default
* Pre-process tables using built in and [custom functions](https://docs.aws.amazon.com/quicksight/latest/user/working-with-calculated-fields.html) and filters, or SQL.
* Some features only available in [Enterprise edition](https://docs.aws.amazon.com/quicksight/latest/user/upgrading-subscription.html) e.g. scheduled reports
* Can programatically create dashboards [via API](https://aws.amazon.com/blogs/big-data/evolve-your-analytics-with-amazon-quicksights-new-apis-and-theming-capabilities/?icmpid=product_whatsnew)

## Redshift
* https://aws.amazon.com/redshift/
* Amazon Redshift is a fast, scalable data warehouse that can extend queries to S3

## Route 53
* https://aws.amazon.com/route53/
* Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets – and can also be used to route users to infrastructure outside of AWS
* route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1

## S3
* https://aws.amazon.com/s3/
* Bucket file storage
* [tinys3](https://www.smore.com/labs/tinys3/) -> small lib for uploading files to S3
* Need to be confident you understand all the access policies and security

## SageMaker
* ML & Jupyter notebooks
* [amazon-sagemaker-examples](https://github.com/awslabs/amazon-sagemaker-examples)
* Fast.ai on sagemaker [setup instructions](https://course.fast.ai/start_sagemaker.html)
* [Get started training and deploying ML](https://aws.amazon.com/getting-started/tutorials/build-train-deploy-machine-learning-model-sagemaker/)
* [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk)
* [SageMaker Studio extends the JupyterLab interface](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-ui.html)
* Label ground truth [with mechanical turk](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
* [SageMaker Neo](https://aws.amazon.com/sagemaker/neo/) -> train machine learning models once and run them anywhere in the cloud and at the edge (Greengrass)
* kernels for Jupyter that provide support for R, Python 2 and 3, Apache MXNet, TensorFlow, and PySpark. Currently does not support tensorflow 2
* [Build end-to-end machine learning workflows with Amazon SageMaker and Apache Airflow](https://aws.amazon.com/blogs/machine-learning/build-end-to-end-machine-learning-workflows-with-amazon-sagemaker-and-apache-airflow/)
* [A Deep Dive Into AWS SageMaker](https://towardsdatascience.com/amazon-machine-learning-a-deep-dive-into-aws-sagemaker-a97897553e05)

## Secrets manager
* Store credentials on AWS
* Usage with jupyter -> http://veekaybee.github.io/2020/02/25/secrets/

## Simple Notification Service (SNS)
* https://aws.amazon.com/sns/
* fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications
* Use when you need to 'fan out' messages to lots of endpoints simultaneously. No guarantee of message delivery

## Simple Queue Service (SQS)
* Stores data in a queue to be retrieved by applications (equivalent to RabbitMQ)
* Data is persisted but must be polled
* https://aws.amazon.com/getting-started/tutorials/send-messages-distributed-applications/?trk=gs_card

## Step Functions
* https://docs.aws.amazon.com/step-functions/
* AWS Step Functions makes it easy to coordinate the components of distributed applications as a series of steps in a visual workflow. You can quickly build and run state machines to execute the steps of your application in a reliable and scalable fashion.
* Since lambdas are stateless, use step functions to coordinate

## Timestream
* https://aws.amazon.com/timestream/
* Time series db
* built-in analytic functions such as smoothing, approximation, and interpolation
* 1/10th the cost of relational databases
* SQL-like queries
* [Grafana support in enterprise](https://grafana.com/grafana/plugins/grafana-timestream-datasource)

## Virtual Private Cloud (VPC)
* Use Amazon Virtual Private Cloud (Amazon VPC) to create a private network for resources such as databases, cache instances, or internal services.
* In AWS, VPC is free to use

# IOT 
* Aws have a variety of products in their IOT ecosystem -> https://aws.amazon.com/iot/
* [Good intro article](https://blogs.itemis.com/en/a-serverless-iot-backend-with-aws-iot)

## IOT Core 
* https://aws.amazon.com/iot-core/
* The core functionality comprising a range of services, included a [message broker](https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html) supporting MQTT and REST
* [Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) can be triggered on MQTT topics, e.g. to trigger a lambda function
* [Official python API](https://github.com/aws/aws-iot-device-sdk-python) or just use paho MQTT, eg in [this article](https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41)
* To get your device certificates (including `root-CA.crt`) from the IOT console select `Onboard -> Configure a device -> Download connection kit`

## IoT Analytics
* https://aws.amazon.com/iot-analytics/
* TLDR: a 'one stop shop' solution, but at the expense of giving up control e.g. over data store
* Ingest data via MQTT or via an API. Filter, transform, and enrich data before storing it in a time-series data store for analysis
* Raw readings are stored in a data store, and sent to pipelines for ETL
* Lambda functions for processing
* Jupyter notebooks for Sophisticated Analytics and Machine Learning 
* Dashboarding with Quicksight

## IOT Events
* https://aws.amazon.com/iot-events/
* TLDR: similar to IFTTT
* define the logic for each event using simple ‘if-then-else’ statements, and select the alert or custom action to trigger when an event occurs.

## IoT Things Graph
* https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-whatis.html
* Similar to node-red -> rules engine
* An orchestration service that simplifies development of IoT applications. These applications can use different devices and web services from different manufacturers that otherwise can't speak with each other 
* There are three key concepts in AWS IoT Things Graph: model, mapping, and flow. 

## Greengrass
* [Greengrass](https://aws.amazon.com/greengrass/)
* AWS IOT services at the edge, no network connection required -> run on a local hub. 
* [Greengrass features](https://aws.amazon.com/greengrass/features/)
* [Docker image](https://hub.docker.com/r/amazon/aws-iot-greengrass)

## FreeRTOS
* https://aws.amazon.com/freertos/
* IoT operating system for microcontrollers, e.g. [ESP32](https://devices.amazonaws.com/detail/a3G0L00000AANtjUAH/ESP32-DevKitC)
* [Github](https://github.com/aws/amazon-freertos)
* [List of supported hardware](https://devices.amazonaws.com/search?page=1&sv=freertos)

## IOT references
* [Using AWS Lambda with Timescale Cloud for IoT Data](https://blog.timescale.com/blog/using-aws-lambda-with-timescale-cloud-for-iot-data/)
* [Build a Visualization and Monitoring Dashboard for IoT Data with Amazon Kinesis Analytics and Amazon QuickSight](https://aws.amazon.com/blogs/big-data/build-a-visualization-and-monitoring-dashboard-for-iot-data-with-amazon-kinesis-analytics-and-amazon-quicksight/)
* [Visualizing Sensor Data in Amazon QuickSight](https://aws.amazon.com/blogs/compute/visualizing-sensor-data-in-amazon-quicksight/)
* [Useful summary of IOT approaches](https://www.reddit.com/r/aws/comments/acf982/how_do_i_decide_which_cloud_platformservices_to/)

## Certification
* [Data scientist](https://aws.amazon.com/training/learning-paths/machine-learning/data-scientist/)

## Books
* [Getting started on AWS (pdf)](https://awsdocs.s3.amazonaws.com/gettingstarted/latest/awsgsg-intro.pdf)
* [AWS best practices](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf)
* [The Good parts of AWS](https://danielvassallo.com/) - PAID
