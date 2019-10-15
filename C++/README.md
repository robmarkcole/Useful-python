## C++
* C++ is widely used for high performance applications, but also on embedded devices such as esp8266
* As of 2019, C++ is now the fourth most popular programming language, behind Java, C, and Python
* [Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
* [Getting started tutorials](http://www.cplusplus.com/doc/tutorial/)

## C++ versions
* C++11 is the third edition (2011)
* C++14 is the fourth edition (December 2014)
* C++17 is the fifth edition.

## Cling - Jupyter kernel
* Jupyter kernel (linux and OS X) -> https://github.com/QuantStack/xeus-cling 
* `conda install -c conda-forge xeus-cling`
* [Good article](https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92)

## VScode
* [Official docs](https://code.visualstudio.com/docs/cpp/config-clang-mac)
* [Read](https://medium.com/gdplabs/build-and-debug-c-on-visual-studio-code-for-mac-77e05537105e) -> had [this issue](https://stackoverflow.com/questions/46342411/wchar-h-file-not-found)
* To build the exe can either [create](https://code.visualstudio.com/docs/cpp/config-clang-mac#_create-a-build-task) a `tasks.json` (or could run from the terminal e.g. `g++ print_number.cpp -o print_number` but probably not 'best practice')

## C vs. C++
* The major difference between C and C++ is that C is a procedural (function driven) programming language and does not support classes and objects, while C++ is a combination of both procedural and object oriented programming language; therefore C is a subset of C++
* [Major differences listed here](http://cs-fundamentals.com/tech-interview/c/difference-between-c-and-cpp.php)