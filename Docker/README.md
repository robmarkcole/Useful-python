## General Docker info
* Getting started -> https://docs.docker.com/docker-for-mac/
* [Dockerhub](https://hub.docker.com/) for discovering containers
* [Portainer](https://www.portainer.io/) for container management from a GUI, run with `docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`
* For browsing containers there is the [Kitematic](https://github.com/docker/kitematic)
* [Ports in docker](https://stackoverflow.com/questions/50278632/what-does-localhost-means-inside-a-docker-container)

## Docker-compose
* Compose is a tool for defining and running multi-container Docker applications -> https://docs.docker.com/compose/
* You use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration


## docker-py
* https://github.com/docker/docker-py

## Raspberry pi
* [Can install docker on pi](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

## Hypriot
* For a whole OS based on docker checkout [hypriot](https://blog.hypriot.com/getting-started-with-docker-and-mac-on-the-raspberry-pi/)
* To flash with wifi support -> https://github.com/hypriot/blog/issues/60
* Require ARM compatible images, see -> https://hub.docker.com/u/hypriot/
