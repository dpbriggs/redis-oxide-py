#!/usr/bin/env python
import os
from setuptools import setup

from redis import __version__


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='redis-oxide',
    version=__version__,
    description='Python client for redis-oxide key-value store',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/andymccurdy/redis-py',
    author='Andy McCurdy',
    author_email='sedrik@gmail.com',
    maintainer='Andy McCurdy',
    maintainer_email='sedrik@gmail.com',
    keywords=['Redis', 'key-value store'],
    license='MIT',
    packages=['redis'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    extras_require={
        'hiredis': [
            "hiredis>=0.1.3",
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
