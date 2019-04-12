## AWS
* https://aws.amazon.com/products

AWS products in alphabetical order:

### Cloud9
* https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html
* Web IDE, runs on EC2 instance

### Data Pipeline
* https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html
* ETL orchestrator

### DynamoDB
* https://aws.amazon.com/dynamodb/
* NoSQL
* DynamoDB is [free for your first 25 GB](https://aws.amazon.com/free/) or [download a local Docker version](https://hub.docker.com/r/amazon/dynamodb-local)
* [Rekognition with dynamoDB backend](https://read.acloud.guru/building-an-imgur-clone-part-2-image-rekognition-and-a-dynamodb-backend-abc9af300123)
* Tables can be created from python [using boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)

### EC2
* https://aws.amazon.com/ec2/
* On demand compute

### Elastic Beanstalk
* https://aws.amazon.com/elasticbeanstalk/
* An easy-to-use service for deploying and scaling web applications and services 

### Elasticsearch
* https://aws.amazon.com/elasticsearch-service/what-is-elasticsearch/
* Search engine

### Kibana
* a free, open-source visualization tool. You can run Kibana on-premises, on Amazon EC2, or on Amazon Elasticsearch Service.
* [Run with docker](https://opendistro.github.io/for-elasticsearch-docs/docs/kibana/#run-kibana-using-docker)

### Kinesis
* https://aws.amazon.com/kinesis/
* Easily collect, process, and analyze video and data streams in real time
* [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/)

### Lambda
* https://aws.amazon.com/lambda/
* Functions in the cloud, can be written in python etc
* [Python walkthrough](https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html) & [python official docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
* [Deploy Sklearn to Lambda](https://github.com/ryansb/sklearn-build-lambda)

### Redshift
* https://aws.amazon.com/redshift/
* Amazon Redshift is a fast, scalable data warehouse that can extend queries to S3

### S3
* https://aws.amazon.com/s3/
* Bucket file storage

### SageMaker
* ML & Jupyter notebooks
* [amazon-sagemaker-examples](https://github.com/awslabs/amazon-sagemaker-examples)
* Fast.ai on sagemaker [setup instructions](https://course.fast.ai/start_sagemaker.html)

### Simple Notification Service (SNS)
* https://aws.amazon.com/sns/
* fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications

### Simple Queue Service (SQS)
* Stores data in a queue to be retrieved by applications (equivalent to RabbitMQ)
* https://aws.amazon.com/getting-started/tutorials/send-messages-distributed-applications/?trk=gs_card


# IOT 
Aws have a variety of products in their IOT ecosystem -> https://aws.amazon.com/iot/

## IOT Core 
* [Developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)
* [Official python API](https://github.com/aws/aws-iot-device-sdk-python) or just use paho, eg in [this article](https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41)
* To get your device certificates (including `root-CA.crt`) from the IOT console select `Onboard -> Configure a device -> Download connection kit`

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

## IoT Analytics
* https://aws.amazon.com/iot-analytics/
* Hosted analytics platform, enabling querying and visualisation of data, e.g. filtered by MQTT topic
