from setuptools import setup

setup(
    name='optics_tools',
    version='0.1',
    url='http://...optics_tools',
    keywords='optics',
    author='Robin Cole',
    author_email='robmarkcole@gmail',
    description='Tools for satellite optics',
    packages=[
        "optics_tools"
    ],
    install_requires=[
        'astropy',
        'numpy',
        'matplotlib',
    ]
)
