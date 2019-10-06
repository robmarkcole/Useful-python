## OpenFASS

* https://www.openfaas.com/
* Functions as a service -> each function is run in a Docker container and containers are managed by OpenFASS
* Write functions in any language for Linux or Windows and package in Docker/OCI image format
* There is a 'store' for functions published by the community, e.g. face detection, colorization
* Walkthrough -> https://blog.alexellis.io/quickstart-openfaas-cli/
* Docker swarm docs -> https://docs.openfaas.com/deployment/docker-swarm/ -> to leave the swarm `docker swarm leave --force`
* [Getting started with python example](https://blog.alexellis.io/first-faas-python-function/) -> start the script with `./deploy_stack.sh --no-auth`
* Image processing example, using Minio -> https://github.com/alexellis/function-storage-example
* Colorize an image using a store function -> https://blog.alexellis.io/colorise-your-cats-with-openfaas/

Usage: 
```
$ curl localhost:8080/function/hello-python -d "it's Alex here"

Hello! You said: its Alex here
```

* https://github.com/f43i4n/faas-mqtt-connector -> It currently only has basic MQTT functionality and few configuration options, but it may fulfil your needs or you could create a PR to improve the connector.