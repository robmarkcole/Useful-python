## Dask
* Dask is a flexible library for parallel computing in Python. Dask represents parallel computations with task graphs. These directed acyclic graphs may have arbitrary structure, which enables both developers and users the freedom to build sophisticated algorithms and to handle messy situations not easily managed by the map/filter/groupby paradigm common in most data engineering frameworks.
* http://docs.dask.org/en/latest/
* Run on laptop or cluster
* https://github.com/TomAugspurger/dask-tutorial-pycon-2018
* https://github.com/ipython/ipyparallel/blob/master/examples/dask.ipynb
* https://towardsdatascience.com/trying-out-dask-dataframes-in-python-for-fast-data-analysis-in-parallel-aa960c18a915
* [Distributed image processing using Dask] (http://www.gilgalad.co.uk/post/dask-distributed/)

## Dask Image
* https://dask-image.readthedocs.io/en/latest/
* Image processing with Dask Arrays

## Dask vs Spark
* Generally Dask is smaller and lighter weight than Spark. This means that it has fewer features and instead is intended to be used in conjunction with other libraries, particularly those in the numeric Python ecosystem.
* http://docs.dask.org/en/latest/spark.html

## Dask Geospatial
* Geospatial Operations at Scale with Dask and Geopandas