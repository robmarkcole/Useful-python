## Grafana
* https://grafana.com/
* [Grafana playground](https://play.grafana.org)
* Grafana is an open source visualization tool that can be used on top of a variety of different data stores but is most commonly used together with Graphite, InfluxDB, and also Elasticsearch and Logz.io.

## Plugins
* [Various plugins](https://grafana.com/plugins) including [plot.ly](https://grafana.com/grafana/plugins/natel-plotly-panel), [floorplan data](https://grafana.com/grafana/plugins/pierosavi-imageit-panel), 

## Python
* Several python libs including https://github.com/m0nhawk/grafana_api and https://github.com/weaveworks/grafanalib

## Example usage
* [home-monitoring-with-mqtt-influxdb-grafana](http://nilhcem.com/iot/home-monitoring-with-mqtt-influxdb-grafana)
* [Arduino docker-mqtt-grafana-influxdb-python](https://dzone.com/articles/playing-with-docker-mqtt-grafana-influxdb-python-a)
* [Monitor air quality with a pycom board](https://kapusta.cc/2018/02/02/air-quality-monitor-revisited/)
* [Real time video analytics with Redis](https://github.com/RedisGears/EdgeRealtimeVideoAnalytics)

## Managed
* https://aws.amazon.com/grafana/

### Graqfana vs Kibana
[The key difference](https://logz.io/blog/grafana-vs-kibana/) between the two visualization tools stems from their purpose. Grafana is designed for analyzing and visualizing metrics such as system CPU, memory, disk and I/O utilization. Grafana does not allow full-text data querying. Kibana, on the other hand, runs on top of Elasticsearch and is used primarily for analyzing log messages.

## References
* [TimescaleDB and Grafana](https://blog.timescale.com/grafana-time-series-exploration-visualization-postgresql-8c7baa9c3bfe/)
* [Postgres for IOT thread](https://community.grafana.com/t/postgres-schema-for-iot-sensors/14449) and [another here](https://community.particle.io/t/postgres-schema-for-iot-sensors/47821). TLDR -> include everything in your db that might help you understand your data later on
* [Time-series Analysis with TimescaleDB, Grafana and Plotly](https://corpglory.com/s/timescaledb-grafana-plotly-time-series-analysis/)