# Useful-python
Python code and Jupyter notebooks for reference.

## Run locally with docker
Run a [notebook server in docker](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), mounting in this directory with:
```
docker run --rm -p 8888:8888 \
                -e JUPYTER_ENABLE_LAB=yes \
                -e AWS_ACCESS_KEY_ID=xyz \
                -e AWS_SECRET_ACCESS_KEY=aaa \
                -v "$PWD":/home/jovyan/work \
                --name jupyter \
                jupyter/scipy-notebook:latest
```
Then run `docker logs jupyter` to extract the url & token and place these in your browser (something like `http://127.0.0.1:8888/?token=33ebd`), or [use vscode to connect](https://code.visualstudio.com/docs/python/jupyter-support#_connect-to-a-remote-jupyter-server). When you are finished `docker stop jupyter`. Alternative environments are listed on https://github.com/jupyter/docker-stacks