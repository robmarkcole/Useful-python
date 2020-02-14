[![Sponsor](https://img.shields.io/badge/sponsor-%F0%9F%92%96-green)](https://github.com/sponsors/robmarkcole)

# Useful-python
Python code and Jupyter notebooks for reference.

## Run with docker
Run a [notebook server in docker](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), mounting in this directory with:
```
$ docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/scipy-notebook:17aba6048f44
```

## ✨ Support this work

https://github.com/sponsors/robmarkcole

If you or your business find this work useful please consider becoming a sponsor at the link above, this really helps justify the time I invest in maintaining this repo. As we say in England, 'every little helps' - thanks in advance! 