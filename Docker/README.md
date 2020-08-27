## Docker
* [Getting started with python and docker](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/)
* Excellent docker intro -> https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5

## Docker-compose
* Compose is a tool for defining and running multi-container Docker applications -> https://docs.docker.com/compose/
* You use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration
* [dockerize-a-flask-celery-and-redis-application-with-docker-compose](https://nickjanetakis.com/blog/dockerize-a-flask-celery-and-redis-application-with-docker-compose)
* [Simple tutorial on docker compose with flask](http://containertutorials.com/docker-compose/flask-compose.html)

## Dockerhub
* [How to push](https://stackoverflow.com/questions/28349392/how-to-push-a-docker-image-to-a-private-repository#28349540)
* [My profile](https://hub.docker.com/u/robmarkcole)

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

## Docker networking
* [Ports in docker](https://stackoverflow.com/questions/50278632/what-does-localhost-means-inside-a-docker-container)