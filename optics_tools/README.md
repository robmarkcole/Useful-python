* Helper tools for satellite optics.
* To understand how the package is structured see http://docs.python-guide.org/en/latest/writing/structure/#modules
* To install in editable mode install with >> `pip install -e .` from within the folder containing `setup.py`
* Use [black](https://github.com/ambv/black) to format code before committing `black filename.py`
* To run tests with py.test and pytest-cov plugin:
```
(C:\ProgramData\Anaconda3) C:\Users\RCole\Documents\optics_tools>py.test --cov tests/
============================= test session starts =============================
platform win32 -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: C:\Users\RCole\Documents\Bitbucket\optics_tools, inifile:
plugins: hypothesis-3.23.0, cov-2.5.1
collecting 0 items
collecting 35 items
collected 35 items


tests\test_core.py ...................................

----------- coverage: platform win32, python 3.6.2-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
tests\__init__.py        0      0   100%
tests\test_core.py      95      0   100%
----------------------------------------
TOTAL                   95      0   100%


========================== 35 passed in 0.94 seconds ==========================
```
