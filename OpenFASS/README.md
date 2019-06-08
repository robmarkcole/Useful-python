## OpenFASS

* https://www.openfaas.com/
* Functions as a service -> each function is run in a Docker container and containers are managed by OpenFASS
* Write functions in any language for Linux or Windows and package in Docker/OCI image format
* Walkthrough -> https://blog.alexellis.io/quickstart-openfaas-cli/
* [Getting started with python example](https://blog.alexellis.io/first-faas-python-function/)
* Image processing example, using Minio -> https://github.com/alexellis/function-storage-example
* Colorize an image using a store function -> https://blog.alexellis.io/colorise-your-cats-with-openfaas/

Usage: 
```
$ curl localhost:8080/function/hello-python -d "it's Alex here"

Hello! You said: its Alex here
```