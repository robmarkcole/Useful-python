## Redis
* Redis is an in-memory database that persists on disk. The data model is key-value, but many different kind of values are supported: Strings, Lists, Sets, Sorted Sets, Hashes, HyperLogLogs, Bitmaps. 
* Redis stands for REmote DIctionary Server
* Use case -> cache SQL query results
* `brew install redis` then `$ redis-server`
* https://redis.io/ and [online example](http://try.redis.io/)
* [AnimalRecognitionDemo](https://github.com/RedisGears/AnimalRecognitionDemo) -> dont forget to use python 2 commands, runs but did not detect the cat images
* [Video processing](https://redislabs.com/blog/my-other-stack-is-redisedge/)
* [scalable-keras-deep-learning-rest-api](https://www.pyimagesearch.com/2018/01/29/scalable-keras-deep-learning-rest-api/)

## Redis Gears
* https://oss.redislabs.com/redisgears/
* Dynamic execution framework for your Redis data, e.g. `GearsBuilder().filter(filter_function).map(map_function).groupby(key_extractor_function, reducer_function).run('*')`

## RedisAi
* https://oss.redislabs.com/redisai/
* RedisAI is a Redis module for serving tensors and executing deep learning models.
* https://github.com/RedisAI/redisai-py

## RedisTimeSeries
* https://oss.redislabs.com/redistimeseries/
* RedisTimeSeries is a Redis Module adding a Time Series data structure to Redis.
* https://github.com/RedisTimeSeries/redistimeseries-py

## RedisEdge
* https://redislabs.com/solutions/redisedge/
* Edge Computing Database for the IoT Edge