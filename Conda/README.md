## Conda jupyter kernels
* List conda envs with `conda env list` and activate with `conda activate my_env`
* Install https://github.com/Anaconda-Platform/nb_conda_kernels to use conda envs from jupyter. It is necessary to ensure each env has ipykernel installed:
```
conda install -n my_env ipykernel
```
