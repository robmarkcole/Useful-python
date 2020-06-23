## LightGBM (microsoft) A Highly Efficient Gradient Boosting Decision Tree
* https://lightgbm.readthedocs.io/en/latest/index.html
* LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient. It is C code exposed via CLI using .conf files, or via a python wrapper
* Seen in many kaggle kernels -> https://github.com/microsoft/LightGBM/tree/master/examples
* Already in Colab notebooks but not utilising GPU, need to 'recompile with CMake option -DUSE_GPU=1'. Takes a long time, royal pain in the arse, spent an hour trying receiving various errors and gave up, just use CPU.
* [For time series forecasting](https://github.com/microsoft/forecasting/blob/master/examples/grocery_sales/python/00_quick_start/lightgbm_single_round.ipynb)