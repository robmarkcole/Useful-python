## Docker
* [Getting started with python and docker](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/)
* [Ports in docker](https://stackoverflow.com/questions/50278632/what-does-localhost-means-inside-a-docker-container)

## Docker-compose
* Compose is a tool for defining and running multi-container Docker applications -> https://docs.docker.com/compose/
* You use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration
* [dockerize-a-flask-celery-and-redis-application-with-docker-compose](https://nickjanetakis.com/blog/dockerize-a-flask-celery-and-redis-application-with-docker-compose)

## Portainer 
* [Portainer](https://www.portainer.io/) for container management from a GUI, run with `docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`

## docker-py
* Python api for docker -> https://github.com/docker/docker-py

## Raspberry pi
* [Can install docker on pi](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

## Hypriot
* For a whole OS based on docker checkout [hypriot](https://blog.hypriot.com/getting-started-with-docker-and-mac-on-the-raspberry-pi/)
* To flash with wifi support -> https://github.com/hypriot/blog/issues/60
* Require ARM compatible images, see -> https://hub.docker.com/u/hypriot/

## Balena
* https://www.balena.io/
* Manage fleets of IOT devices using docker

## VScode
* [Develop in a Docker container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
* Python example -> https://github.com/microsoft/vscode-remote-try-python

## Useful docker commands
* debug the docker image locally on my dev machine, first build `docker build -t $yourimage .` then run `docker run -it --entrypoint=/bin/bash $yourimage`