## Prophet
* https://facebook.github.io/prophet/
* Used by [AWS Forecast](https://aws.amazon.com/forecast/)
* Installation: On Mac use `conda install -c conda-forge fbprophet`

## Model
* Time series forecasting with seasonality - model effects of holidays etc. [Read the paper](https://peerj.com/preprints/3190/)

<p align="center">
<img src="https://github.com/robmarkcole/Useful-python/blob/master/Prophet/model.jpg" width="600">
</p>

## Examples
* [Prophet model with date and number of bike rentals using kaggle dataset](https://towardsdatascience.com/forecast-model-tuning-with-additional-regressors-in-prophet-ffcbf1777dda)
* [forecast hourly energy use with kaggle dataset](https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-prophet)
* [Basic modelling of holidays on sales](https://towardsdatascience.com/predicting-sales-with-python-a-comprehensive-guide-with-facebooks-prophet-1faf092a84e1)
* [Advanced sales prediction with prophet and XGboost](https://www.kaggle.com/elenapetrova/time-series-analysis-and-forecasts-with-prophet) with [github repo](https://github.com/datageekette/rossmann_TSA_forecasts)

## Serving with Flask
* https://towardsdatascience.com/serving-prophet-model-with-flask-predicting-future-1896986da05f
* [Prophet rest server](https://github.com/scirag/fbprophet-rest-docker)

## Docker
* Docker container -> https://github.com/robmarkcole/docker-prophet
* [Example dockerfile](https://github.com/Christmas20191225/notebook/blob/master/Dockerfile)