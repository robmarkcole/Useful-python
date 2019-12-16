## CPython
* The reference implementation of python, which is a mixture of C and python. 
* https://en.wikipedia.org/wiki/CPython and https://en.wikipedia.org/wiki/CPython
* CPython compiles Python code into bytecode before interpreting it
* CPython makes use of a global interpreter lock (GIL) on each CPython interpreter process, which means that within a single process only one thread may be processing Python bytecode at any one time
* In real world applications, situations where the GIL is a significant bottleneck are quite rare. This is because Python is an inherently slow language and is generally not used for CPU-intensive operations such as image-processing or neural networks. Python is typically used at the top level and calls functions in libraries to perform specialized tasks.