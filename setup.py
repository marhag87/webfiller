#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='Webfiller',
    version='0.1.0',
    description='Interface between Google Chrome and pass',
    author='Martin Hagstrom',
    author_email='marhag87@gmail.com',
    url='https://github.com/marhag87/webfiller',
    packages=[
        'webfiller',
    ],
    install_requires=[
        'pyyamlconfig',
    ],
)