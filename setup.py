from setuptools import setup, find_packages

setup(
    name='ensverif',
    version='10.0.0',
    packages=find_packages(include=['ensverif', 'ensverif.*']),
)