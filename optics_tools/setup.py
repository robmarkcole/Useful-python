from setuptools import setup

setup(
    name='optics_tools',
    version='0.1',
    url='http://ariane.sstl.co.uk:7990/projects/OP/repos/optics_tools',
    keywords='optics',
    author='Robin Cole',
    author_email='robin.cole@sstl.co.uk',
    description='Tools for the optics team',
    packages=[
        "optics_tools"
    ],
    install_requires=[
        'astropy',
        'numpy',
        'matplotlib',
    ]
)
