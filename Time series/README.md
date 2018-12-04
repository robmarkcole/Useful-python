## Time series
A number of techniques are popular for analysis of time series data, both classical and deep learning techniques.
* [Intro to time series modelling](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3)
* [More comprehensive tutorial](https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/)


## Prophet
* [Library from Facebook](https://facebook.github.io/prophet/docs/quick_start.html)
* I remember many headaches getting this setup. Use a conda env. Have fun.
* Compared to ARIMA:
  * Fast: with the time to build one ARIMA model I can run several Prophet models
  * Accuracy: it is accurate enough for quick analytical tasks that don’t require high accuracy
  * Simple: it is very simple to use and configure, making the entire experience better
* [Forecasting USD-MNT Exchange Rate](https://medium.com/mongolian-data-stories/forecasting-usd-mnt-exchange-rate-part-1-prophet-4e95ecadf9b2)
* [Forecasting demand](https://www.kaggle.com/myster/eda-prophet-winning-solution-3-0)

## Bayesian techniques
* [STAN docs give intro to several techniques](http://mc-stan.org/docs/bayes-stats-stan/time-series-chapter.html)
* ARIMA - Stats test for stationarity, find p & q parameters. [Simple intro](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)

## Deep learning
* https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
* https://github.com/sagarmk/Forecasting-on-Air-pollution-with-RNN-LSTM
