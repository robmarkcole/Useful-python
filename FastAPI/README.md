## FastAPI
* https://fastapi.tiangolo.com/
* FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. Handles conversion to/from json, type checks
* [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi)
* Run the example and access from another machine with `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
* [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)

## ML and data sci
* https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece -> https://github.com/shanesoh/deploy-ml-fastapi-redis-docker
* [FastAPI and Scikit-Learn: Easily Deploy Models](http://nickc1.github.io/api,/scikit-learn/2019/01/10/scikit-fastapi.html)
* https://towardsdatascience.com/build-and-host-fast-data-science-applications-using-fastapi-823be8a1d6a0
* https://towardsdatascience.com/a-step-by-step-tutorial-to-build-and-deploy-an-image-classification-api-95fa449f0f6a

## Deploy to AWS
* https://towardsdatascience.com/deployment-could-be-easy-a-data-scientists-guide-to-deploy-an-image-detection-fastapi-api-using-329cdd80400 (EC2)
* [Python FastAPI and AWS Lambda Container](https://guillaume-braibant.medium.com/python-fastapi-and-aws-lambda-container-3e524c586f01)

## On raspberry pi
* Installs fine, used on https://github.com/robmarkcole/tensorflow-lite-rest-server

## fastapi-html
* Article -> https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/
* Code -> https://github.com/eugeneyan/fastapi-html

## Issues
* On uploading image `post request causes 400 Bad Request`, [resolved](https://stackoverflow.com/questions/62429244/uploading-images-in-fastapi-post-request-causes-400-bad-request) with `pip install python-multipart`