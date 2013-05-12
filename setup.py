#!/usr/bin/env python
from distutils.core import setup

setup(
    name='python-ipinfodb',
    version='0.1',
    description='This client library to simplify calls to IPInfoDB - Free Geolocation tools for IP Location, API, database and fraud detection tools.',
    author='Martin Alderete',
    url='https://github.com/malderete/python-ipinfodb',
    license='MIT',
    py_modules=[
        'ipinfodb',
    ],
    long_description=open("README").read(),
    classifiers=[
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
