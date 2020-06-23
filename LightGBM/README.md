## LightGBM (microsoft) A Highly Efficient Gradient Boosting Decision Tree. TLDR use XGBoost instead
* https://lightgbm.readthedocs.io/en/latest/index.html
* LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient. It is C code exposed via CLI using .conf files, or via a python wrapper
* Seen in many kaggle kernels -> https://github.com/microsoft/LightGBM/tree/master/examples
* Already installed in Colab notebooks but **not** utilising GPU. Setting up GPU is a royal pain in the arse, spent an hour trying receiving various errors and gave up, just use CPU.
* [For time series forecasting](https://github.com/microsoft/forecasting/blob/master/examples/grocery_sales/python/00_quick_start/lightgbm_single_round.ipynb)

## LightGBM vs XGBoost
* In practice very similar to XGBoost -> https://datascience.stackexchange.com/questions/18903/lightgbm-vs-xgboost
* Many older articles citing LightGBM speed advantage but this may not be true anymore
* Looks far simpler to [use XGBoost with GPU](https://towardsdatascience.com/running-xgboost-on-google-colab-free-gpu-a-case-study-841c90fef101)