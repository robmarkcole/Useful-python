Running [with Docker](https://github.com/OpenGeoscience/geonotebook/tree/master/devops/docker). Note that this [container](https://github.com/OpenGeoscience/geonotebook/blob/master/Dockerfile) has a py27 env. 

docker run -p 8888:8888 -v /Users/robincole/Documents/Github/Useful-python:/notebooks  -it --rm geonotebook