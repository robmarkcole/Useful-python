## InfluxDB
* https://www.influxdata.com/
* InfluxDB is the open source time series database (no-sql) AND the name of the company. A [stack](https://portal.influxdata.com/downloads/) consisting of several pieces of software is is required for configuration of data ingestion, web Ui etc
* InfluDB is just the db, by default on port 8086
* Telegraf is required for collecting and writing data to InfluxDB, using [various plugins](https://www.influxdata.com/products/integrations/) including [mqtt-monitoring](https://www.influxdata.com/integration/mqtt-monitoring/) and [postgresql](https://www.influxdata.com/integration/postgresql-monitoring/)
* Chronograf provides the web UI and visualisation -> [docker instructions](https://hub.docker.com/_/chronograf)
* Kapacitor adds data processing and alerting

## Docker
Run influxdb with Chronograf web UI - note that port 8888 is used by Jupyter so replace `-p 2222:8888`
```
docker network create influxdb

docker run -p 8086:8086 -p 8083:8083 -d \
      -v influxdb:/var/lib/influxdb \
      --net=influxdb \
       --name influxdb \
      influxdb

docker run -p 8888:8888 \
      --net=influxdb \
      chronograf --influxdb-url=http://influxdb:8086
```

## References
* [python client](https://github.com/influxdata/influxdb-python)
* [InfluxDB cloud includes a free Hobbby plan](https://www.influxdata.com/influxcloud-pricing/)
* [Home assistant integration](https://www.home-assistant.io/components/influxdb/)
* [InfluxDB and Grafana for sensor time series](https://thingsmatic.com/2017/03/02/influxdb-and-grafana-for-sensor-time-series/)
* Both InfluxDB and Grafana work great on a Raspberry Pi without using much resources.