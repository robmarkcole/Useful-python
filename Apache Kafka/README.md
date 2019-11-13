## Kafka
* Kafka = A distributed streaming platform
* Apache Kafka is an event streaming platform that combines messaging, storage, and processing of data to build highly scalable, reliable, secure, and real-time infrastructure. Those who use Kafka often use Kafka Connect as well to enable integration with any source or sink. Kafka Streams is also useful, because it allows continuous stream processing.
* https://kafka.apache.org/

### Confluent
* An event streaming platform powered by apache kafka to help companies harness their high volume real-time data streams.
* Docker images -> https://hub.docker.com/u/confluentinc/
* [Quickstart](https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html)
* Extends functionality of Kafka, e.g. to support MQTT -> https://docs.confluent.io/current/connect/kafka-connect-mqtt/index.html

## KSQL
* Confluent KSQL is the streaming SQL engine that enables real-time data processing against Apache Kafka
* https://www.confluent.io/product/ksql/

## References
* [Race tracking with Kafka KSQL, MQTT & Kibana](https://medium.com/@simon.aubury/did-i-beat-ben-race-tracking-with-kafka-ksql-mqtt-kibana-25e62e8ecaef) -> Uses Kafka (MQTT) connect from confluent
* [Apache Kafka and MQTT: End-to-End IoT Integration](https://dzone.com/articles/apache-kafka-mqtt-end-to-end-iot-integration-githu)
* [Apache Kafka Connect MQTT Source Tutorial](https://howtoprogram.xyz/2016/07/30/apache-kafka-connect-mqtt-source-tutorial/)
* [Data Stream Processing for Newbies with Kafka, KSQL, and Postgres](https://medium.com/high-alpha/data-stream-processing-for-newbies-with-kafka-ksql-and-postgres-c30309cfaaf8)
* Can pipe data from Home Assistant into Kafka -> https://www.home-assistant.io/components/apache_kafka/
* Asyncio kafka -> https://github.com/aio-libs/aiokafka
* [Kafka vs redis streams](https://hackernoon.com/introduction-to-redis-streams-133f1c375cd3) TLDR redis has less overhead and better for projects which dont require scale