from setuptools import setup

setup(
    name='optics_tools',
    version='0.1',
    url='https://github.com/robmarkcole/Useful-python/tree/master/optics_tools',
    keywords='optics',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for ptics',
    packages=[
        "optics_tools"
    ],
    install_requires=[
        'astropy',
        'numpy',
        'matplotlib',
    ]
)
