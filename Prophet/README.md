## Prophet
* https://facebook.github.io/prophet/
* Used by [AWS Forecast](https://aws.amazon.com/forecast/) and available [in Mode](https://mode.com/notebooks/)
* Installation: On Mac use `conda install -c conda-forge fbprophet`
* With pip Pystan installs ok, but fbprophet usually fails. Use conda

## Model
* Time series forecasting with seasonality - model effects of holidays etc. [Read the paper](https://peerj.com/preprints/3190/)

<p align="center">
<img src="https://github.com/robmarkcole/Useful-python/blob/master/Prophet/model.jpg" width="600">
</p>

* VS ARIMA -> the Prophet authors claim 'ARIMA forecasts are prone to large trend errors when there is a change in trend near the cutoff period and they fail to capture any seasonality'. Also it requires expert level experience to tune ARIMA models. In contrast Pophet is 'designed to have intuitive parameters  that  can  be  adjusted  without  knowing  the  details  of  the  underlying  model'

## Examples
* [forecast hourly energy use with kaggle dataset](https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-prophet)
* [Basic modelling of holidays on sales](https://towardsdatascience.com/predicting-sales-with-python-a-comprehensive-guide-with-facebooks-prophet-1faf092a84e1)
* [Advanced sales prediction with prophet and XGboost](https://www.kaggle.com/elenapetrova/time-series-analysis-and-forecasts-with-prophet) with [github repo](https://github.com/datageekette/rossmann_TSA_forecasts)

## Docker
* https://github.com/robmarkcole/streamlit_forecasting_app

## Serving with Flask
* https://towardsdatascience.com/serving-prophet-model-with-flask-predicting-future-1896986da05f
* [Prophet rest server](https://github.com/scirag/fbprophet-rest-docker)