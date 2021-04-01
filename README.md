# Useful-python
Python code and Jupyter notebooks for reference.

## Run locally with docker
Run a [notebook server in docker](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), mounting in this directory with:
```
docker run --rm -p 8888:8888 \
                -e JUPYTER_ENABLE_LAB=yes \
                -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                -v "$PWD":/home/jovyan/work \
                --name jupyter \
                jupyter/scipy-notebook:latest
```
Then run `docker logs jupyter` to extract the url & token and place these in your browser (something like `http://127.0.0.1:8888/?token=33ebd`), or [use vscode to connect](https://code.visualstudio.com/docs/python/jupyter-support#_connect-to-a-remote-jupyter-server). When you are finished `docker stop jupyter`. 

Alternative environments are listed on https://github.com/jupyter/docker-stacks. I use `scipy-notebook` when only python is required, or `datascience-notebook` if R or Julia are required. 

Note in the example above we are passing in environment variables from the host. To set an env var on host OSX: `echo 'export ENV_VAR=12345' >> ~/.zprofile` (or `~/.bash_profile`)