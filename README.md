# Useful-python
Python code and Jupyter notebooks for reference.

## Run locally with docker
Run a [notebook server in docker](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), mounting in this directory with:
```
$ docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/scipy-notebook
```