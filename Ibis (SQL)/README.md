## Ibis
* https://docs.ibis-project.org/ & https://github.com/ibis-project/ibis
* [Intro article](https://labs.quansight.org/blog/2020/06/ibis-an-idiomatic-flavor-of-sql-for-python-programmers/)
* TLDR write python that converts to SQL, return pandas dataframes
* pandas loads the data into the memory of the local host, and performs the computations on it. Ibis instead, leaves the data in its storage, and performs the computations there. 
* VS pure SQL: as the complexity of operations grow, SQL can become very difficult to deal with. With Ibis, you can take fully advantage of software engineering techniques to keep your code readable and maintainable, while writing very complex analitics code.