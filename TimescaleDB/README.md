## TimescaleDB
* Postgres extension, optimised for time-series, [open source (and enterprise)](https://www.timescale.com/enterprise)
* https://github.com/timescale/timescaledb
* [Article: why relational for IOT](https://blog.timescale.com/use-relational-database-instead-of-nosql-for-iot-application/) -> SQL for familiarity and heritage, schemas for complex queries, eliminate data silos
* [Tutorials](https://docs.timescale.com/v1.2/tutorials)
* Run with docker - just stop local postgres server first to prevent port conflict
* [local or cloud hosting](https://www.timescale.com/pricing), also [Azure](https://blog.timescale.com/timescale-microsoft-azure-team-up-to-power-iot-and-time-series-workloads/) and [AWS](https://blog.timescale.com/tutorial-installing-timescaledb-on-aws-c8602b767a98/)
* TimescaleDB basically organizes and indexes data in chunks of time, called buckets, which allows for really fast retrieval when performing range queries. Tables made this way are called hypertables.

## Timescale cloud
* Cheapest pricing around $2.3 daily for 20 GB
* They will also host Grafana for you

## PGSchema
* PGSchema is an easy-to-use tool that helps you generate a schema for PostgreSQL and TimescaleDB. 
* [link](https://pgschema.com/?utm_source=timescale-december-2019&utm_medium=email&utm_campaign=newsletter&utm_content=pg-schema&_hsenc=p2ANqtz-_622gTgE3zxbF4yVmXYISDVA-RQJ3Ot4prQouDIRWl8PePGurxZHgIBrwdFssFskpExcEQZRu-5CItQm47HKoEw5vDAQ&_hsmi=81089501)

## Air quality demo
* https://github.com/timescale/examples/tree/master/air-quality
* Presented in [this article](https://blog.timescale.com/blog/simplified-time-series-analytics-using-the-time_bucket-function/)

## RPi
* TimescaleDB cannot be installed on an RPi -> `doesn't support architecture 'arm64'` -> see [this issue](https://github.com/timescale/timescaledb-docker/issues/25)
* [Tutorial using timescale cloud](https://blog.timescale.com/tutorials/how-to-store-sensor-data-from-a-raspberry-pi-into-postgresql/) and [the code](https://github.com/timescale/examples/tree/master/pi-light)

## Home Assistant
* [Custom integration supporting timescale](https://github.com/freol35241/ltss)