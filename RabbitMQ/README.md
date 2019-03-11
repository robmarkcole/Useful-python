## RabbitMQ
* RabbitMQ is a message broker.
* [Python intro](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) using [Pika](https://pika.readthedocs.io/en/0.11.0/#)
* On mac [install](https://www.rabbitmq.com/install-homebrew.html) with Homebrew

## RabbitMQ vs Redis
After evaluating both Redis and RabbitMQ I chose RabbitMQ as our broker [for the following reasons](https://stackoverflow.com/questions/29539443/redis-vs-rabbitmq-as-a-data-broker-messaging-system-in-between-logstash-and-elas):

1. RabbitMQ allows you to use a built in layer of security by using SSL certificates to encrypt the data that you are sending to the broker and it means that no one will sniff your data and have access to your vital organizational data.
2. RabbitMQ is a very stable product that can handle large amounts of events per seconds and many connections without being the bottle neck.
3. In our organization we already used RabbitMQ and had good internal knowledge about using it and an already prepared integration with chef.

## Redis, Apache Kafka & RabbitMQ
* [Read](https://donchev.is/post/redis-kafka-ra)