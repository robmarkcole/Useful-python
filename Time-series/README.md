## Time series
TLDR: understand whether there is autocorrelation or not, mean is changing with time, and variance with time, then employ appropriate feature engineering
* Various python packages for ts -> https://tslearn.readthedocs.io/en/stable/integration_other_software.html
* [Intro to time series modelling](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3)
* [More comprehensive tutorial](https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/)
* [Awesome time-series anomaly detection](https://github.com/rob-med/awesome-TS-anomaly-detection)
* Consider LightGBM (in Microsoft folder) -> https://github.com/microsoft/forecasting
* [Finding correlations in time series data](https://erdem.pl/2020/06/finding-correlations-in-time-series-data)
* [Forecasting Time Series with Multiple Seasonalities using TBATS in Python](https://medium.com/intive-developers/forecasting-time-series-with-multiple-seasonalities-using-tbats-in-python-398a00ac0e8a)

## Arima
* https://towardsdatascience.com/advanced-time-series-analysis-with-arma-and-arima-a7d9b589ed6d

## Prophet
* [Library from Facebook](https://facebook.github.io/prophet/docs/quick_start.html)
* I remember many headaches getting this setup. Use a conda env. Have fun.
* Compared to ARIMA:
  * Fast: with the time to build one ARIMA model I can run several Prophet models
  * Accuracy: it is accurate enough for quick analytical tasks that don’t require high accuracy
  * Simple: it is very simple to use and configure, making the entire experience better
* [Forecasting USD-MNT Exchange Rate](https://medium.com/mongolian-data-stories/forecasting-usd-mnt-exchange-rate-part-1-prophet-4e95ecadf9b2)
* [Forecasting demand](https://www.kaggle.com/myster/eda-prophet-winning-solution-3-0)

## Darts
* https://github.com/unit8co/darts
* High level wrapper to many ts methods
* Many dependencies, including prophet, but did eventually install in docker via pip

## Bayesian techniques
* [STAN docs give intro to several techniques](http://mc-stan.org/docs/bayes-stats-stan/time-series-chapter.html)
* ARIMA - Stats test for stationarity, find p & q parameters. [Simple intro](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)

## Deep learning
* https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
* https://github.com/sagarmk/Forecasting-on-Air-pollution-with-RNN-LSTM
* https://www.notion.so/Corrupt-sparse-irregular-and-ugly-Deep-learning-on-time-series-887b823df439417bb8428a3474d939b3

## Concepts
* Autocorrelation: also known as serial correlation, is the correlation of a signal with a delayed copy of itself as a function of delay.
* correlogram: is an image of correlation statistics, an ACF plot