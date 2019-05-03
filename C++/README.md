* Jupyter kernel (linux and OS X) -> https://github.com/QuantStack/xeus-cling ([try in Binder](https://mybinder.org/v2/gh/QuantStack/xeus-cling/stable?filepath=notebooks/xcpp.ipynb))
* [Good article](https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92)
* C++ is widely used for high performance applications, but also on embedded devices such as esp8266
* [Getting started tutorials](http://www.cplusplus.com/doc/tutorial/)

## Cling
* Interpreted C++ -> https://cdn.rawgit.com/root-project/cling/master/www/index.html

## VScode
* [Official docs](https://code.visualstudio.com/docs/cpp/config-clang-mac)
* [Read](https://medium.com/gdplabs/build-and-debug-c-on-visual-studio-code-for-mac-77e05537105e) -> had [this issue](https://stackoverflow.com/questions/46342411/wchar-h-file-not-found)
* To build the exe can either [create](https://code.visualstudio.com/docs/cpp/config-clang-mac#_create-a-build-task) a `tasks.json` (or could run from the terminal e.g. `g++ print_number.cpp -o print_number` but probably not 'best practice')