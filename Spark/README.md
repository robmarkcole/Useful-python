# Spark
* TLDR: tool for processing data in parallel across a cluster, works in-memory.
* [Intro to pyspark](https://towardsdatascience.com/a-brief-introduction-to-pyspark-ff4284701873)
* API in python and scala. [Intro read omn tradeoffs](https://www.datacamp.com/community/tutorials/apache-spark-python)
* [pyspark docs](https://spark.apache.org/docs/0.9.0/python-programming-guide.html)
* Understand [hadoop vs spark](https://logz.io/blog/hadoop-vs-spark/)
* Get started on a hosted env for freee on databricks -> https://databricks.com/
* [Geospatial Analytics at Scale with Deep Learning and Apache Spark](https://databricks.com/session/geospatial-analytics-at-scale-with-deep-learning-and-apache-spark)

## Spark Dataframes
The key data type used in PySpark is the Spark dataframe. This object can be thought of as a table distributed across a cluster and has functionality that is similar to dataframes in R and Pandas. If you want to do distributed computation using PySpark, then you’ll need to perform operations on Spark dataframes, and not other python data types.

It is also possible to use Pandas dataframes when using Spark, by calling `toPandas()` on a Spark dataframe, which returns a pandas object. However, this function should generally be avoided except when working with small dataframes, because it pulls the entire object into memory on a single node.

One of the key differences between Pandas and Spark dataframes is eager versus lazy execution. In PySpark (**lazy**), operations are delayed until a result is actually needed in the pipeline. For example, you can specify operations for loading a data set from S3 and applying a number of transformations to the dataframe, but these operations won’t immediately be applied. Instead, a graph of transformations is recorded, and once the data is actually needed, for example when writing the results back to S3, then the transformations are applied as a single pipeline operation. This approach is used to avoid pulling the full data frame into memory and enables more effective processing across a cluster of machines. With Pandas (**eager**) dataframes, everything is pulled into memory, and every Pandas operation is immediately applied.

## Geo data
* Geo Spatial Data Analytics on Spark -> https://github.com/harsha2010/magellan
* [GeoSpark](http://geospark.datasyslab.org/) -> GeoSpark is a cluster computing system for processing large-scale spatial data. GeoSpark extends Apache Spark / SparkSQL with a set of out-of-the-box Spatial Resilient Distributed Datasets (SRDDs)/ SpatialSQL that efficiently load, process, and analyze large-scale spatial data across machines.