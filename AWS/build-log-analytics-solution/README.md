## Overview
* https://aws.amazon.com/getting-started/projects/build-log-analytics-solution/?trk=gs_card
* This solution will typically cost $367.74 per month


* Set up a Kinesis Agent on data sources to collect data and send it continuously to Amazon Kinesis Firehose.
* Create an end-to-end data delivery stream using Kinesis Firehose. The delivery stream will transmit your data from the agent to (destinations including Amazon Kinesis Analytics, Amazon Redshift, Amazon Elasticsearch Service, and Amazon S3.
* Process incoming log data using SQL queries in Amazon Kinesis Analytics.
* Load processed data from Kinesis Analytics to Amazon Elasticsearch Service to index the data.
* Analyze and visualize the processed data using [Kibana](https://www.elastic.co/products/kibana)

## Services
* [Amazon Kinesis](https://aws.amazon.com/kinesis/) is a platform for streaming data on AWS, offering powerful services to make it easy to load and analyze streaming data, and also enables you to build custom streaming data applications for specialized needs. It offers two services: Amazon Kinesis Firehose, and Amazon Kinesis Streams.
* Amazon Kinesis Firehose is the easiest way to load streaming data into AWS. It can capture and automatically load streaming data into Amazon S3 and Amazon Redshift, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It enables you to quickly implement an ELT approach, and gain benefits from streaming data quickly.