## Conda jupyter kernels
* List conda envs with `conda env list` and activate with `conda activate my_env`
* Install https://github.com/Anaconda-Platform/nb_conda_kernels to use conda envs from jupyter. It is necessary to ensure each env has ipykernel installed:
```
conda install -n my_env ipykernel
```

## Conda Docker
* Official image -> https://hub.docker.com/r/conda/miniconda3
* https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754