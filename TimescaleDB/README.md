## TimescaleDB
* Postgres extension, optimised for time-series, [open source (and enterprise)](https://www.timescale.com/enterprise)
* https://github.com/timescale/timescaledb
* [Article: why relational for IOT](https://blog.timescale.com/use-relational-database-instead-of-nosql-for-iot-application/) -> SQL for familiarity and heritage, schemas for complex queries, eliminate data silos
* [Tutorials](https://docs.timescale.com/v1.2/tutorials)
* [Integrate with Promethius](https://docs.timescale.com/v1.2/tutorials/prometheus-adapter)
* [local or cloud hosting](https://www.timescale.com/pricing), also [Azure](https://blog.timescale.com/timescale-microsoft-azure-team-up-to-power-iot-and-time-series-workloads/) and [AWS](https://blog.timescale.com/tutorial-installing-timescaledb-on-aws-c8602b767a98/)
* TimescaleDB basically organizes and indexes data in chunks of time, called buckets, which allows for really fast retrieval when performing range queries. Tables made this way are called hypertables.

## Air quality demo
* https://github.com/timescale/examples/tree/master/air-quality
* Presented in [this article](https://blog.timescale.com/blog/simplified-time-series-analytics-using-the-time_bucket-function/)