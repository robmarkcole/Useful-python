## Papermill
* https://github.com/nteract/papermill
* https://papermill.readthedocs.io/en/latest/
* Parameterize, execute, and analyze notebooks
* [Used by Netflix](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233)
* The two ways to execute the notebook with parameters are: (1) through the Python API (e.g from another notebook) and (2) through the command line interface.
* In classic notebook, add the `parameters` tag to a cell in Jupyter, `View > Cell Toolbar > Tags`
* In Jupyterlab have the cell tab as below:

<p align="center">
<img src="https://github.com/robmarkcole/Useful-python/blob/master/Papermill/tag_cell.png" width="700">
</p>

* Create input.ipynb, then run from command line:
```
(C:\ProgramData\Anaconda3) C:\Users\RCole\Documents\Bitbucket\robin_cole\Python_
Packages_Examples\papermill>papermill input.ipynb output.ipynb -p alpha 2 -p ratio 1
Input Notebook:  input.ipynb
Output Notebook: output.ipynb
100%|¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 4/4 [00:00<00:00, 83.32it/s]
```
* `output.ipynb` is generated with the `injected-parameters`

## Python API
For example:
```Python
import papermill as pm

pm.execute_notebook(
   'path/to/input.ipynb',
   'path/to/output.ipynb',
   parameters = dict(alpha=0.6, ratio=0.1)
)
```
