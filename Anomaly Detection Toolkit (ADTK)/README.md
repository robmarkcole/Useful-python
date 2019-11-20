## Anomaly Detection Toolkit (ADTK)
* https://arundo-adtk.readthedocs-hosted.com/en/latest/index.html
* Anomaly Detection Toolkit (ADTK) is a Python package for unsupervised / rule-based time series anomaly detection.
* Use case of repo mainter ([Arduno](https://www.arundo.com/)) is detecting faults in equipment
* Very succint overview of [types of anomalies](https://arundo-adtk.readthedocs-hosted.com/en/latest/userguide.html) in the user guide

As the nature of anomaly varies over different cases, a model may not work universally for all anomaly detection problems. Choosing and combining detection algorithms (`detectors`), feature engineering methods (`transformers`), and ensemble methods (`aggregators`) properly is the key to build an effective anomaly detection model.

This package offers a set of common detectors, transformers and aggregators with unified APIs, as well as pipe classes that connect them together into a model. It also provides some functions to process and visualize time series and anomaly events.

## The Numenta Anomaly Benchmark (NAB)
* https://github.com/numenta/NAB
* This repository contains the data and scripts which comprise the Numenta Anomaly Benchmark (NAB) v1.1. NAB is a novel benchmark for evaluating algorithms for anomaly detection in streaming, real-time applications. It is composed of over 50 labeled real-world and artificial timeseries data files plus a novel scoring mechanism designed for real-time applications.